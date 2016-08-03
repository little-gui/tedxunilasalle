from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = list(Post.objects.all()[:5])
    posts_count = len(posts)
    for i in range(posts_count+1, 6):
        posts.append('')

    return render(request, 'home/index.html', {'posts': posts})


def contact(request):
    sent = False

    if request.method == 'POST':
        send_mail(
            '[TEDxUnilasalleCanoas] %s <%s>' % (
                request.POST.get('name'), 
                request.POST.get('email')
            ),
            request.POST.get('message'),
            settings.EMAIL_DEFAULT_FROM,
            [settings.EMAIL_DEFAULT_TO],
            fail_silently=True
        )
        sent = True

    return render(request, 'home/contact.html', {'sent': sent})

