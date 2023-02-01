from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import The_best_blog
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class The_best_blogListView(ListView):
    model = The_best_blog

class The_best_blogDetailView(DetailView):
    model = The_best_blog

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.numbers_of_views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class The_best_blogCreateView(CreateView):
    model = The_best_blog
    fields = ('header', 'content', 'slug')
 #   template_name = 'blog/the_best_blog_form.html'
#    success_url = reverse_lazy('blog:draft')



class The_best_blogUpdateView(UpdateView):
    model = The_best_blog
    fields = ('header', 'content', 'slug')
    success_url = reverse_lazy('blog:draft')

class The_best_blogDeleteView(DeleteView):
    model = The_best_blog
    fields = ('header', 'content')
    success_url = reverse_lazy('blog:draft')


def draft(request):
    context = {
        'object_list': The_best_blog.objects.all()
    }
    return render(request, 'blog/the_best_blog_draft.html', context)

def change_status(request, slug):
    blog_item = get_object_or_404(The_best_blog, slug=slug)
    if blog_item.sign_of_publication == '1':
        blog_item.sign_of_publication = '0'
    else:
        blog_item.sign_of_publication = '1'
    blog_item.save()
    return redirect(reverse('blog:draft'))