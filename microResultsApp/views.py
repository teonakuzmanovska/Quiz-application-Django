from django.shortcuts import render, redirect

# Create your views here.
from microResultsApp.models import *


def quiz(request):
    if request.method == "POST":

        questions = QuestionModel.objects.all()
        points = 0

        for q in questions:
            if q.ans == request.POST.get(q.question):
                points += 1
        #  ako vekje e reshen testot izbrishi gi poenite, pa stavi gi novite
        if ResultsModel.objects.count():
            ResultsModel.objects.all().delete()

        result = ResultsModel(points=points)
        result.save()

        # return render(request, 'results.html')
        return redirect('results')

    else:
        questions = QuestionModel.objects.all()
        context = {"questions": questions}
        return render(request, 'quiz.html', context=context)


def results(request):
    points = ResultsModel.objects.all()
    context = {"points": points}
    return render(request, 'results.html', context=context)
