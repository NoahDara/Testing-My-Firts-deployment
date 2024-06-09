
# from django.db.models.signals import post_migrate, post_save
# from django.dispatch import receiver
# from accounts.models.users import User
# from helpers.handlers.emails import SendEmailHandler
# from ..models import SiteDomain
# from django.urls import reverse
# from loguru import logger

# @receiver(post_save, sender=User, dispatch_uid="create_new_user")
# def create_new_user_handler(sender, instance, created, **kwargs):
#     if created:
#         try:
#             email_handler = SendEmailHandler()
#             template_name = "account/password_set_email.html"
#             subject = "Welcome to EPR - Set Your Password"
#             receiver = instance.email
#             site_domain_object = SiteDomain.objects.all().first()
#             user_uid = email_handler.generate_uid_from_id(id=instance.id)
#             redirect_url = f"{site_domain_object.__str__()}/{reverse('set-password', kwargs={'user_uid': user_uid})}"
#             data = {
#                 "full_name": f"{instance.first_name} {instance.last_name}",
#                 "set_password_url": redirect_url
#             }
#             is_sent = email_handler.send_email(
#                 template=template_name, subject=subject, receiver=receiver, kwargs=data
#             )
#             logger.info(f"{instance.get_full_name()} email sent: {is_sent}")
#         except Exception as er:
#             logger.error(f"Signal `create_new_user_handler()` raised error: {er}")
