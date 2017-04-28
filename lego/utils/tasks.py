from smtplib import SMTPException

from structlog import get_logger

from lego import celery_app

from .email import EmailMessage

log = get_logger()


@celery_app.task(bind=True, max_retries=5)
def send_email(self, **kwargs):
    """
    Generic task to send emails with retries.
    """
    message = EmailMessage(**kwargs)

    try:
        message.send()
    except SMTPException as e:
        log.error('email_task_exception', exc_info=True, extra=kwargs)
        raise self.retry(exc=e, countdown=2 ** self.request.retries)