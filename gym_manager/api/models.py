from django.db import models

class Exercise(models.Model):
    name=models.CharField(max_length=50)
    difficulty=models.CharField(max_length=20,choices=[('beginner','beginner'),('intermediate','intermediate'),('advanced','advanced')])
    reps=models.IntegerField()
    sets=models.IntegerField()

    def __str__(self):
        return  self.name

class Client(models.Model):
    name=models.CharField(max_length=40,null=False)
    age=models.IntegerField()
    weight=models.IntegerField()
    height=models.IntegerField()
    sex=models.CharField(max_length=10,choices=[('male','Male'),('female','Female')])
    exercises=models.ManyToManyField(Exercise)
    def __str__(self):
        return  self.name
    
class Trainer (models.Model):
    x=list(Exercise.objects.values_list('id', 'name'))
    y=list(Client.objects.values_list('id', 'name'))
    ex_id=models.CharField(choices=x)
    c_id=models.CharField(choices=y)