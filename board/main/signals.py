from datetime import datetime, timedelta

from django.core.signals import request_finished
from django.dispatch import receiver

from main.models import Advert


@receiver(request_finished)
def set_adverts_inactive(sender, **kwargs) -> None:
    current_date = datetime.now()
    active_adverts = Advert.objects.filter(is_active=True, created_at__lte=current_date - timedelta(days=30))
    active_adverts.update(is_active=False)