from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.apps import AppConfig


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_courses')

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    
    def check_course_completion(self):
        total_lessons = self.course.lessons.count()
        completed_lessons = LessonCompletion.objects.filter(student=self.student, lesson__course=self.course).count()
        self.is_completed = total_lessons == completed_lessons
        if self.is_completed:
            self.rating = self.calculate_rating()
            print(f"Course {self.course.title} is completed by {self.student.username}")
        self.save()
        
    def calculate_rating(self):
        #Rating calculation logic
        total_lessons = self.course.lessons.count()
        completed_lessons = LessonCompletion.objects.filter(student=self.student, lesson__course=self.course).count()
        rating = (completed_lessons / total_lessons) * 100 if total_lessons > 0 else 0
        return rating
    
class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'

    def ready(self):
        from django.contrib.auth.models import Group
        Group.objects.get_or_create(name='Teachers')
        Group.objects.get_or_create(name='Students')

class LessonCompletion(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_lessons')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='completions')
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} completed {self.lesson.title}"