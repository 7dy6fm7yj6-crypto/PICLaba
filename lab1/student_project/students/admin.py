from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'display_exams', 'display_marks', 'average_mark')
    list_filter = ('name', 'surname')
    search_fields = ('name', 'surname')
    
    def display_exams(self, obj):
        return obj.exams
    display_exams.short_description = 'Экзамены'
    
    def display_marks(self, obj):
        return obj.marks
    display_marks.short_description = 'Оценки'
    
    def average_mark(self, obj):
        return f"{obj.get_average_mark():.2f}"
    average_mark.short_description = 'Средний балл'

admin.site.register(Student, StudentAdmin)