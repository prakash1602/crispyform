from django.db import models

# Create your models here.
class College(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Institute(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Location(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Branch(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class StudentDetails(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    marks=models.IntegerField()
    fee=models.IntegerField()
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    institute=models.ForeignKey(Institute,on_delete=models.CASCADE)


