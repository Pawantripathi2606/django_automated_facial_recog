from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm

def student_list(request):
    """View to list all students with search functionality"""
    query = request.GET.get('search', '')
    students = Student.objects.all()
    
    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(roll_no__icontains=query)
        )
    
    context = {
        'students': students,
        'search_query': query
    }
    return render(request, 'students/student_list.html', context)


def student_create(request):
    """View to create a new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.name} added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'students/student_form.html', context)


def student_update(request, pk):
    """View to update an existing student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.name} updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    context = {'form': form, 'action': 'Update', 'student': student}
    return render(request, 'students/student_form.html', context)


def student_delete(request, pk):
    """View to delete a student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f'Student {name} deleted successfully!')
        return redirect('student_list')
    
    context = {'student': student}
    return render(request, 'students/student_confirm_delete.html', context)


def student_detail(request, pk):
    """View to see student details"""
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)
