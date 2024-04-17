from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def change_password(username, new_password):
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()


def create(username, email, password):
    user = User.objects.create_user(f"{username}", f"{email}", f"{password}")
    user.save()



