from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.forms import inlineformset_factory
from django import forms
from django.contrib.auth.models import Group, User
from .models import Course, Lesson
from .forms import CourseCreationForm, LessonForm

def home(request):
    # Представление для начальной публичной страницы
    return render(request, 'courses/home.html')

def course_list(request):
    courses = Course.objects.all()
    is_instructor = request.user.groups.filter(name='Teachers').exists() if request.user.is_authenticated else False
    return render(request, 'courses/course_list.html', {'courses': courses, 'is_instructor': is_instructor})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Teacher'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'role', 'password1', 'password2']

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            if role == 'student':
                group = Group.objects.get(name='Students')
            else:
                group = Group.objects.get(name='Teachers')
            user.groups.add(group)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'courses/register.html', {'form': form})

def is_instructor(user):
    return user.groups.filter(name='Teachers').exists()


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']

@user_passes_test(is_instructor)
def create_course(request):
    LessonFormSet = inlineformset_factory(Course, Lesson, form=LessonForm, extra=2, max_num=10)
    if request.method == 'POST':
        course_form = CourseCreationForm(request.POST, request.FILES)
        lesson_formset = LessonFormSet(request.POST, request.FILES)
        if course_form.is_valid() and lesson_formset.is_valid():
            course = course_form.save(commit=False)
            course.instructor = request.user
            course.save()
            lesson_formset.instance = course
            lesson_formset.save()
            return redirect('course_list')
    else:
        course_form = CourseCreationForm()
        lesson_formset = LessonFormSet()
    return render(request, 'courses/create_course.html', {
        'course_form': course_form,
        'lesson_formset': lesson_formset,
    })