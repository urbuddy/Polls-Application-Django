from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from demo.models import Question, Choice
from django.views import generic

# Create your views here.


def index(request):
    latest_q_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_q_list": latest_q_list}
    return render(request, "demo/index.html", context)


class IndexView(generic.ListView):
    template_name = "demo/index.html"
    context_object_name = "latest_q_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")


def details(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, "demo/details.html", {"question": q})


class DetailView(generic.DetailView):
    model = Question
    template_name = "demo/details.html"


def results(request, question_id):
    que = get_object_or_404(Question, id=question_id)
    return render(request, 'demo/results.html', {'question': que})


class ResultView(generic.DetailView):
    model = Question
    template_name = "demo/results.html"


def votes(request, question_id):
    que = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = que.choice_set.get(id=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'demo/details.html', {'question': que, 'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('demo:results', args=(que.id,)))


def create(request):
    if request.method == 'POST':
        que = Question()
        que.question_text = request.POST['question']
        que.pub_date = timezone.now()
        que.save()
        question = Question.objects.get(pk=que.pk)
        if question is not None:
            question.choice_set.create(choice_text=request.POST['option1']).save()
            question.choice_set.create(choice_text=request.POST['option2']).save()
            question.choice_set.create(choice_text=request.POST['option3']).save()
            question.choice_set.create(choice_text=request.POST['option4']).save()
        else:
            print(que.question_text, " question is empty")
        return redirect('demo:index')
    return render(request, "demo/create.html")
