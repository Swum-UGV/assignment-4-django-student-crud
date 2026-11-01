from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
def home(request):
    students=Student.objects.all()
    return render(request,'students/home.html',{'students':students})
def add_student(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        gender=request.POST['gender']
        phone=request.POST['phone']
        Student.objects.create(name=name,email=email,gender=gender,phone=phone)
        return redirect('home')
    return render(request,'students/add_student.html')
def edit_student(request,student_id):
    student=get_object_or_404(Student,id=student_id)
    if request.method=="POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.gender = request.POST['gender']
        student.phone = request.POST['phone']
        student.save()
        return redirect('home')
    return render(request,'students/edit_student.html',{'student':student})
def delete_student(request,student_id):
    student=get_object_or_404(Student,id=student_id)
    student.delete()
    return redirect('home')
