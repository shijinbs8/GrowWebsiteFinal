from django.db import models

class TeamMembersModel(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
class Projects(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.TextField()


    def __str__(self) -> str:
        return self.name
