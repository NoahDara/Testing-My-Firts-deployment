from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils.encoding import smart_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import mimetypes
from decouple import config
from django.conf import settings
from django.contrib.auth import get_user_model
import random, string
from decouple import config
from loguru import logger



class SendEmailHandler:
    def generate_uid_from_id(self, id: int):
        """Generates UID from db primary keys for security in terms of integrity and send emails with that UID."""
        return urlsafe_base64_encode(smart_bytes(id))

    def decode_uid_to_id(self, uid):
        """Deconstruction of the UID to its original db primary key."""
        return smart_str(urlsafe_base64_decode(uid))

    def send_email(
        self,
        template: str,
        subject: str,
        receiver: str | list,
        attachments: list = [],
        sender: str = settings.DEFAULT_FROM_EMAIL,
        **kwargs,
    ) -> bool:
        """Sends emails with a rendered html."""
        try:
            message = get_template(f"{template}").render(kwargs["kwargs"])

            mail = EmailMessage(
                subject=f"{subject}",
                body=message,
                from_email=f"{sender}",
                to=[receiver],
            )
            mail.content_subtype = "html"

            # Attach the documents to the email
            for attachment_path in attachments:
                content_type, encoding = mimetypes.guess_type(attachment_path)
                if content_type is None:
                    content_type = "application/octet-stream"
                with open(attachment_path, "rb") as attachment:
                    mail.attach(
                        filename=attachment_path.split("/")[-1],
                        content=attachment.read(),
                        mimetype=content_type,
                    )

            mail.send()
            logger.success(f"Email: {receiver}, sent successfully.")
            return True
        except Exception as e:
            logger.error(f"Email: {receiver}, failed with error: {e}")
            return False