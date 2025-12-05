from django.shortcuts import render
from .models import Student

def filter_students(request):
    students = Student.objects.all()
    threshold = request.GET.get('threshold')
    
    if threshold:
        try:
            threshold = float(threshold)
            filtered_students = []
            for student in students:
                if student.get_average_mark() > threshold:
                    filtered_students.append(student)
            students = filtered_students
        except ValueError:
            
            pass
    
    context = {
        'students': students,
        'threshold': threshold or ''
    }
    return render(request, 'students/filter_students.html', context)