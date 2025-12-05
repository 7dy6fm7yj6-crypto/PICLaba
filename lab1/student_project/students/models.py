from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    exams = models.TextField(verbose_name="Экзамены (через запятую)")
    marks = models.CharField(max_length=100, verbose_name="Оценки (через запятую)")
    
    def get_exams_list(self):
        return [exam.strip() for exam in self.exams.split(',')]
    
    def get_marks_list(self):
        return [int(mark.strip()) for mark in self.marks.split(',')]
    
    def get_average_mark(self):
        marks_list = self.get_marks_list()
        return sum(marks_list) / len(marks_list) if marks_list else 0
    
    def __str__(self):
        return f"{self.name} {self.surname} - Средний балл: {self.get_average_mark():.2f}"
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"