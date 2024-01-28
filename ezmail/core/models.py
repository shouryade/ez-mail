from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


# Create your models here.


class User(models.Model):
    """
    User model for storing user information
    """

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username


def send_email(instance):
    """
    Sends an email to the user
    """
    # Setting my email credentials
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("PASSWORD")

    recipient_email = instance.email

    subject = "Welcome!"
    body = "Dear {},\n\nThank you for registering with FunStuff with Shourya.".format(
        instance.username
    )

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Establish a connection to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent to the user {}".format(instance.username))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for the user
    """
    if created:
        send_email(instance)
    else:
        print("User value saved!")
