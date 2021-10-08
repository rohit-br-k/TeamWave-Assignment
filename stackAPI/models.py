from django.db import models

# Create your models here.

class Data(models.Model):
    question = models.CharField(max_length=500)
    vote = models.IntegerField(default=0)
    views = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Data"
        verbose_name_plural ="Datas"