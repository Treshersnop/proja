from django.contrib import admin
from django.utils.safestring import mark_safe

from core import models


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name')
    search_fields = ('username', 'last_name', 'first_name')


@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_photo')
    search_fields = ('first_name', 'last_name')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="60" height="60" />'
            )

    get_photo.short_description = 'Avatar'
    get_photo.allow_tags = True


@admin.register(models.Pupil)
class Pupil(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(models.Grade)
class Grade(admin.ModelAdmin):
    list_display = ('numeral', 'character')
    search_fields = ('numeral',)


@admin.register(models.Subject)
class Subject(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Club)
class Club(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.TeacherSubject)
class TeacherSubject(admin.ModelAdmin):
    list_display = ('teacher', 'subject', 'club',)


@admin.register(models.Tutor)
class Tutor(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'numeral', 'character')
