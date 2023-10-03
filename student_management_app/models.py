from urllib import request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render



class CustomUser(AbstractUser):
    user_type_data = ((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=18)
    pass
                               
    

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    classroom_link = models.URLField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)  # Corrigir o nome do campo para 'gender'
    profile_pic = models.FileField()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    address = models.TextField()
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField(Subjects)
    objects = models.Manager()
    

    
class StudentResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

    
    



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):# kwargs : permite que você passe qualquer número de argumentos de palavra-chave para a função
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(admin=instance)
        Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_start_year="2023-01-01", session_end_year="2028-01-01", address="", profile_pic="", gender="Masculino")

            
            
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.students.save()

