from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.hello_message(user.email)
        return super().form_valid(form)

    def hello_message(self, user_mail):
        send_mail(
            subject= 'Добро пожаловать в наш каталог',
            message= "Привет, ты зарегистрировался на сайте",
            from_email= EMAIL_HOST_USER,
            recipient_list= [user_mail]
        )
