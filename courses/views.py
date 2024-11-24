from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django import forms
from django.contrib.auth.models import Group, User
from .models import Course, Lesson, Enrollment, LessonCompletion
from .forms import CourseCreationForm, LessonForm

def home(request):
    return render(request, 'courses/home.html')

def course_list(request):
    courses = Course.objects.all()
    is_instructor = request.user.groups.filter(name='Teachers').exists() if request.user.is_authenticated else False
    return render(request, 'courses/course_list.html', {'courses': courses, 'is_instructor': is_instructor})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        return redirect('available_courses')
    
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'back_url': reverse('my_courses')
        })

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
    LessonFormSet = inlineformset_factory(Course, Lesson, form=LessonForm, can_delete=True, extra=2, max_num=10)
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
    
@login_required
@user_passes_test(is_instructor)
def manage_courses(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, 'courses/manage_courses.html', {'courses': courses})

@login_required
@user_passes_test(is_instructor)
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk, instructor=request.user)
    LessonFormSet = inlineformset_factory(Course, Lesson, form=LessonForm, extra=2, max_num=10)

    if request.method == 'POST':
        course_form = CourseCreationForm(request.POST, request.FILES, instance=course)
        lesson_formset = LessonFormSet(request.POST, request.FILES, instance=course)

        if course_form.is_valid() and lesson_formset.is_valid():
            course_form.save()
            lesson_formset.save()
            print("Course and lessons updated successfully.")
            return redirect('manage_courses')
        else:
            print("Errors in Course Form:", course_form.errors)
            print("Errors in Lesson Formset:", lesson_formset.errors)

    else:
        course_form = CourseCreationForm(instance=course)
        lesson_formset = LessonFormSet(instance=course)

    return render(request, 'courses/edit_course.html', {
        'course_form': course_form,
        'lesson_formset': lesson_formset,
        'course': course,
    })


@login_required
def student_dashboard(request):
    # Display all available courses for students
    available_courses = Course.objects.exclude(enrollments__student=request.user)
    enrolled_courses = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/student_dashboard.html', {
        'available_courses': available_courses,
        'enrolled_courses': enrolled_courses,
        'back_url': reverse('home')
    })

@login_required
def join_course(request, course_id):
    # Function for joining a student to a course
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('student_dashboard')

@login_required
def available_courses(request):
    # Show only those courses for which the student has not yet enrolled
    enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('course', flat=True)
    courses = Course.objects.exclude(id__in=enrolled_courses)
    return render(request, 'courses/available_courses.html', {'courses': courses})


@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('my_courses')


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    courses = [enrollment.course for enrollment in enrollments]
    
    return render(request, 'courses/my_courses.html', {
        'courses': courses,
        'back_url': reverse('student_dashboard')
        })


@login_required
def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, pk=course_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id, course=course)

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        return redirect('available_courses')

    # Count the total number of lessons and the number of completed lessons
    total_lessons = course.lessons.count()
    completed_lessons = LessonCompletion.objects.filter(student=request.user, lesson__course=course).count()
    progress = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    
    # Checking if the current lesson is completed
    is_lesson_completed = LessonCompletion.objects.filter(student=request.user, lesson=lesson).exists()

    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'total_lessons': total_lessons,
        'completed_lessons': completed_lessons,
        'progress': progress,
        'is_lesson_completed': is_lesson_completed,
        'back_url': reverse('course_detail', kwargs={'pk': course_id})
    })

@csrf_exempt
@login_required
def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course = lesson.course

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        return JsonResponse({'error': 'You are not enrolled in this course'}, status=403)

    # Mark the lesson as completed
    LessonCompletion.objects.get_or_create(student=request.user, lesson=lesson)

    # Update progress for recording
    total_lessons = course.lessons.count()
    completed_lessons = LessonCompletion.objects.filter(student=request.user, lesson__course=course).count()

    enrollment = Enrollment.objects.get(student=request.user, course=course)
    enrollment.check_course_completion()
    enrollment.progress = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    enrollment.save()

    return JsonResponse({'message': 'Lesson completed successfully!'})