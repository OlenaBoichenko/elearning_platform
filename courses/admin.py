from django.contrib import admin
from .models import Course, Lesson, Enrollment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
