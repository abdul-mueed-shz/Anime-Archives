from rest_framework import viewsets
from apps.posts.api.serializers import PostSerializer
from apps.posts.models import Post


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = [
        'get',
        'post',
        'delete',
        'put',
        'patch'
    ]
