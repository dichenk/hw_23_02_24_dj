from django.urls import path

from blog.apps import BlogConfig
from blog.views import The_best_blogListView, The_best_blogDetailView, draft, The_best_blogCreateView, The_best_blogUpdateView, The_best_blogDeleteView, change_status

app_name = BlogConfig.name
urlpatterns = [
        path('', The_best_blogListView.as_view(), name='list'),
        path('draft/', draft, name='draft',),
        path('<slug:slug>/', The_best_blogDetailView.as_view(), name='blog_detail'),
        path('create/', The_best_blogCreateView.as_view(), name='create'),
        path('update/<slug:slug>/', The_best_blogUpdateView.as_view(), name='update'),
        path('delete/<slug:slug>/', The_best_blogDeleteView.as_view(), name='delete'),
        path('status/<slug:slug>/', change_status, name='status')
]