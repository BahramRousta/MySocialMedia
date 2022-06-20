from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import CommentModel
from .forms import CommentForm
from core.models import Post


def comment(request, post_id):
    username = request.user.username
    post = Post.objects.get(id=post_id)

    # Get all comment
    comments = CommentModel.objects.filter(post_id=post_id,
                                           username=username)
    new_comment = None

    if request.method == 'POST' and request.user.is_authenticated:

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            body = request.POST['body']
            new_comment = CommentModel.objects.create(post_id=post_id,
                                                      username=username,
                                                      body=body)
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'comment.html', {'post': post,
                                            'comments': comments,
                                            'comment_form': comment_form,
                                            'new_comment': new_comment})


@login_required(login_url='signin')
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    current_user = request.user.username

    if request.method == "POST" and post.user == current_user:
        post.delete()
        return HttpResponseRedirect(reverse('core:profile', args=[current_user]))

    return render(request, 'post_list.html', {'post': post})