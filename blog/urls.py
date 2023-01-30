from django.urls import path

from blog.apps import BlogConfig
from blog.views import The_best_blogListView, The_best_blogDetailView, draft, The_best_blogCreateView

app_name = BlogConfig.name
urlpatterns = [
        path('', The_best_blogListView.as_view(), name='list'),
        path('draft/', draft, name='draft',),
        path('<int:pk>/', The_best_blogDetailView.as_view()),
        path('create/', The_best_blogCreateView.as_view(), name='create'),
        ]