from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def contact(request):
    sent = False

    if request.method == 'POST':
        send_mail(
            '[TEDxUnilasalleCanoas] %s <%s>' % (request.POST.get('name'), request.POST.get('email')),
            request.POST.get('message'),
            settings.EMAIL_DEFAULT_FROM,
            [settings.EMAIL_DEFAULT_TO],
            fail_silently=True
        )
        sent = True

    return render(request, 'home/contact.html', {'sent': sent})

