from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import The_best_blog
from django.urls import reverse_lazy
class The_best_blogListView(ListView):
    model = The_best_blog

class The_best_blogDetailView(DetailView):
    model = The_best_blog

class The_best_blogCreateView(CreateView):
    model = The_best_blog
    fields = ('header', 'content')
    success_url = reverse_lazy('blog:draft')

def draft(request):
    context = {
        'object_list': The_best_blog.objects.all()
    }
    return render(request, 'blog/the_best_blog_draft.html', context)