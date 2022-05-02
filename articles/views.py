from django.shortcuts import render
from .api.serializers import ArtticleSerializers
from rest_framework import viewsets
from .models import Article

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArtticleSerializers