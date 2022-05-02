from django.urls import path
from .views import ArticlelistView, ArticleDetailView

urlpatterns =[
    path('', ArticlelistView.as_view()),
    path('/<pk>', ArticleDetailView.as_view()),
]