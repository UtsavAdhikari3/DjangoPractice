from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Choice
from django.shortcuts import render,get_object_or_404
from django.db.models import F
from django.urls import reverse


def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render(request,"polls/index.html",context)


def detail(request, question_id):
    question = get_object_or_404(Questions,pk=question_id)    
    return render(request,"polls/detail.html",{"question":question})
    
def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Questions,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You did not select a question choice."
            },
        )
    
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id)))