from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Article
from .serializers import ArtticleSerializers

class ArticlelistView(ListAPIView):
    queryset= Article.objects.all()
    serializer_class = ArtticleSerializers

class ArticleDetailView(RetrieveAPIView):
    queryset= Article.objects.all()
    serializer_class = ArtticleSerializers