from django.db import models

# Create your models here.


class QuestionModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200, null=True)


class ResultsModel(models.Model):
    category = models.CharField(max_length=200, null=True)
    points = models.IntegerField()
