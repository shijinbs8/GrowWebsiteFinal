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
    
class Tech(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    descriptions=models.TextField()

    def __str__(self) -> str:
        return self.name

class CallBackRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    exported = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name