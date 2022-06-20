from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('comment/<str:post_id>', views.comment, name='comment'),
]