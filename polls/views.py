# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse

from .forms import ContactForm


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
#    return HttpResponse('Your ar looking at question {}'.format(question_id))
    question = get_object_or_404(Question, id=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
#    response = "Your ar watching at results of question {}".format(question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question': question})

def vote(request,question_id):
#   return HttpResponse("U are voting on question {}".format(question_id))
   p = get_object_or_404(Question,pk=question_id)
   print(request.method)
   if request.method == 'POST':
       choice_id = request.POST.get('choice',0)
       try:
           selected_choice = p.choice_set.get(pk=choice_id)
       except Choice.DoesNotExist:
    # Redisplay the question voting form.
           return render(request,'polls/detail.html', {
               'question': p,
	       'error_message': "you didn't select a choice..",
           })
       else:
           selected_choice.votes +=1
           selected_choice.save()
           # Always return on HttpResponseRedirect after successfully dealing
           # with Post data. This prevents data from being posted twice if a 
           # user hits the Back button.
           return HttpResponseRedirect(reverse('results',args=(p.id,)))
   else:
       return HttpResponse('you post question id: %s' % p.id)





def send_mail(request):
    if request.method == 'GET':
        form = ContactForm()
	return render(request, 'polls/sendmail.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    return HttpResponse('subject: %s message: %s sender: %s cc_myself: %s ' % (subject,message,sender,cc_myself))
	else:
	    return render(request, 'polls/sendmail.html', {'form':form})

