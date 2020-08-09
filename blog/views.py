from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post


def post_list(request):
    context = dict()
    context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    context = dict()
    context['post'] = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context)
