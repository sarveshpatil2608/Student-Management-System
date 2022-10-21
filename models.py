from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    objects = None
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    fees = models.IntegerField(default=0)
    paid_fees = models.IntegerField(default=0)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    ad_date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
