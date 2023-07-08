import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import News
from .models import MailingList
from home.models import Movie
from secret_data import secret_email_sender, secret_password


@receiver(post_save, sender=News, )
def func_name(sender, instance, created, **kwargs):
    """Рассылка новостей на почту"""
    if not News.objects.all().latest('time').newsletter:
        email_sender = secret_email_sender
        password = secret_password
        email_getter = list()
        text = News.objects.all().latest('time')

        for i in MailingList.objects.all():
            email_getter.append(i.email)

        smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
        smtp_server.starttls()

        msg = MIMEMultipart()
        msg["From"] = f"Movie-Site <{secret_email_sender}>"
        msg["Subject"] = "Обновились новости на сайте!"
        html = f"""
        <html>
        <head></head>
                <img src="{text.url_image}" alt="" style="margin: 0 auto;">
                <p>{text.title}</p>
                <p>Для полной информации перейдите на сайт <a href="#">https://www.Movie-Site.ru/</a></p>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))

        smtp_server.login(email_sender, password)
        smtp_server.sendmail(email_sender, email_getter, msg.as_string())
        text.newsletter = True
        text.save()


@receiver(post_save, sender=Movie, )
def func_name_2(sender, instance, created, **kwargs):
    """Рассылка новых фильмов на почту"""
    if not Movie.objects.all().latest('created').newsletter:
        email_sender = secret_email_sender
        password = secret_password
        email_getter = list()
        movie = Movie.objects.all().latest('created')
        cat = ''
        if movie.category_id == 1:
            cat = 'фильм'
        elif movie.category_id == 2:
            cat = 'сериал'
        else:
            cat = 'мультфильм'

        for i in MailingList.objects.all():
            email_getter.append(i.email)

        smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
        smtp_server.starttls()

        msg = MIMEMultipart()
        msg["From"] = f"Movie-Site <{secret_email_sender}>"
        msg["Subject"] = f"На сайте появился новый {cat}!"
        html = f"""
            <html>
            <head></head>
                    <img src="{movie.url_image}" alt="" width="400" height="600" style="margin: 0 auto;">
                    <p>"{movie.title}"</p>
                    <p>Для полной информации о {cat}е перейдите на сайт <a href="#">https://www.Movie-Site.ru/</a></p>
            </html>
            """
        msg.attach(MIMEText(html, 'html'))

        smtp_server.login(email_sender, password)
        smtp_server.sendmail(email_sender, email_getter, msg.as_string())
        movie.newsletter = True
        movie.save()
