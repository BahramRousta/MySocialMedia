from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import ThreadModel, MessageModel
from .forms import ThreadForm, MessageForm


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        return render(request, 'chat/inbox.html', {'threads': threads})


class CreatThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        return render(request, 'chat/creat_thread.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST['username']

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('chat:thread', pk=thread.pk)
        except:
            return redirect('chat:create_thread')


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)

        return render(request, 'chat/thread.html', {'form': form,
                                                    'thread': thread,
                                                    'message_list': message_list})


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread= ThreadModel.objects.get(pk=pk)

        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(thread=thread,
                               sender_user=request.user,
                               receiver_user=receiver,
                               body=request.POST['message'])
        message.save()

        return redirect('chat:thread', pk=pk)

