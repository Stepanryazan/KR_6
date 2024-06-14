import smtplib
from datetime import datetime

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from mailing.models import Mailing, MailingAttempts


class Command(BaseCommand):

    def handle(self, *args, **options):

        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = datetime.now(zone)
        mailings = Mailing.objects.filter(status='started')
        print(f'Количество рассылок для отправки: {mailings.count()}')

        for mailing in mailings:
            print(f'Рассылка: {mailing.message.subject}')
            clients = mailing.client.all()
            try:
                server_response = send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in clients],
                    fail_silently=False,
                )
                MailingAttempts.objects.create(last_attempt_time=current_datetime,
                                               status=MailingAttempts.SUCCESS,
                                               server_response=server_response,
                                               mailing=mailing, )
            except smtplib.SMTPException as e:
                MailingAttempts.objects.create(last_attempt_time=current_datetime,
                                               status=MailingAttempts.FAIL,
                                               server_response=str(e),
                                               mailing=mailing,
                                               )