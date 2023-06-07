from rest_framework import serializers

from apps.posts.models import Post, STATUS
from apps.user.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(method_name='get_status')

    author_profile = serializers.SerializerMethodField(method_name='get_author', read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'status',
            'author',
            'author_profile'
        ]

    def get_status(self, obj):
        """
        @param obj:
        @return:
        """
        return STATUS[obj.status][1]

    def get_author(self, obj):
        """
        @param obj:
        @return:
        """
        user = UserSerializer(obj.author)
        return user.data
