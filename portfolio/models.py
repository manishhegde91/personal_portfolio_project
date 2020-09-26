from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="portfolio/images/")
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True, blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    #To display the title on the top window.
    def __str__(self):
        return self.title
