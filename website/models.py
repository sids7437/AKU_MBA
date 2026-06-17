from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    email = models.EmailField()
    photo = models.ImageField(upload_to='faculty/')

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='notices/')
    date = models.DateField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    date = models.DateField()

    def __str__(self):
        return self.title