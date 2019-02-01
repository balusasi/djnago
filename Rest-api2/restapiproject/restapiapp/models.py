from django.db import models
class loginmodel(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username