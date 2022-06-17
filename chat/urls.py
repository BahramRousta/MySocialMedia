from django.urls import path
from .views import *

app_name = "chat"

urlpatterns = [
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create_thread', CreatThread.as_view(), name='create_thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create_message', CreateMessage.as_view(), name='create_message'),
]