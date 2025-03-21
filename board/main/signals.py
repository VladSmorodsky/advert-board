from datetime import datetime, timedelta

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from main.models import Advert


@receiver(request_finished)
def set_adverts_inactive(sender, **kwargs) -> None:
    """
    Signal sets adverts inactive after 30 days of their publishing.
    """
    current_date = datetime.now()
    active_adverts = Advert.objects.filter(is_active=True, created_at__lte=current_date - timedelta(days=30))
    active_adverts.update(is_active=False)


@receiver(post_save, sender=Advert)
def advert_created(sender, instance, created, **kwargs):
    """
    Signal is responsible for sending email when advert is created.
    """
    if created:
        context = {
            "advert": instance,
        }
        html_content = render_to_string("emails/advert_created.html", context)
        plain_text = strip_tags(html_content)  # Convert to plain text
        message = EmailMultiAlternatives(f'Advert is published!',
                                         plain_text,
                                         settings.DEFAULT_FROM_EMAIL,
                                         [(instance.user.email)])
        message.attach_alternative(html_content, "text/html")
        message.send()
