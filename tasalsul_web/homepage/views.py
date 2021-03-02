from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            subject = 'Query | Tasalsul'
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            message_raw = form.cleaned_data['message']
            message = name + ' sent the following message of inquiry,' + '\n\n' + message_raw
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            # return redirect("homepage:index") # put in the page to goto after succesful submission over here.
            return redirect("homepage:message_sent")

    return render(request, 'homepage/index.html', {'form': form})

def message_sent(request):
    return render(request, 'homepage/message_sent.html')