from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ChatGroup


def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/index.html', {"registration": users})


def chat_user(request, username):
    user = User.objects.get(username=username)
    users = User.objects.exclude(id=request.user.id)

    chat_group = ChatGroup.objects.filter(users=user).filter(users=request.user).first()

    if not chat_group:
        chat_group = ChatGroup.objects.create(name=f"cht_beetwen_{user.username}_and_{request.user.username}")
        chat_group.users.add(user, request.user)

    data = {
        'user': user,
        'registration': users,
        "chat_group": chat_group,
    }

    return render(request, 'chat/chat.html', context=data)
