from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:20]

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {
# 		'latest_question_list':latest_question_list
# 	}
# 	return render(request, 'polls/index.html', context)


	# c = ""
	# for q in latest_question_list:
	# 	c = c + q.question_text
	# 	print(c)
	# return HttpResponse(c)

		# output =', ' .join([q.question_text for q in latest_question_list])
		# return HttpResponse(output)
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	context = {
# 	 	'question' : question
# 	}
# 	return render(request, 'polls/detail.html', context)

	# try:
	# 	question = Question.objects.get(pk=question_id)
	# 	context = {
	# 	'question' : question
	# }
	# except Question.DoesNotExist:
	# 	raise Http404("Question Doesn't Exist")

	# return render(request, 'polls/detail.html', context)

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	context = {

# 		'question': question
# 	}
# 	return render(request, 'polls/results.html', context)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {

		'question': question,
		'error_message': "you didn't select a choice",
	}
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', context)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))