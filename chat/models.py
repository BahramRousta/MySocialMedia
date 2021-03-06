from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class ThreadModel(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='+')
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='+')


class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel,
                               on_delete=models.CASCADE,
                               related_name='+',
                               blank=True,
                               null=True)
    sender_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='+')
    receiver_user = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='messages_photos', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

