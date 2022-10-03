from django.contrib import admin

# Register your models here.
from microResultsApp.models import *

admin.site.register(QuestionModel)
admin.site.register(ResultsModel)
