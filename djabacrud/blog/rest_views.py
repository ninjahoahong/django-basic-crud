from rest_framework import generics
from blog.serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['post_id'])
