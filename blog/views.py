from django.shortcuts import render

from .models import *
from django.views.generic import ListView, DetailView


class Home(ListView):
    """ Главна страница с постами """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Moschino'
        return context

    def get_queryset(self):
        """ Фильтруем посты которые не черновик """
        return Post.objects.filter(is_published=True)


class GetPost(DetailView):
    """ Вывод отдельного поста """
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def about(request):
    return render(request, 'blog/about.html')