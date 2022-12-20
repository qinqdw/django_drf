from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='学生姓名', help_text='学生姓名')

    class Meta:
        db_table = 'student'