from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
def send_notify(preview,pk,title,subcribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text':preview,
            'link':f'{settings.SITE_URL}/news/{pk}'
        }


    )
    msg = EmailMultiAlternatives(subject=title,body='',from_email=settings.EMAIL_HOST_USER,to=subcribers)
    msg.attach_alternative(html_content,'text/html')
    msg.send()

@receiver(m2m_changed,sender=PostCategory)
def notify_post(sender,instance,**kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subcribers_emails = []

        for item in categories:
            subscribers = item.subscribers.all()
            subcribers_emails += [s.email for s in subscribers]

        send_notify(instance.preview(),instance.pk,instance.title,subcribers_emails)