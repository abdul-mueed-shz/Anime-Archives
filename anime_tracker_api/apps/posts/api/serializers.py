from rest_framework import serializers

from apps.posts.models import Post, STATUS


class PostSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(method_name='get_status')
    author = serializers.SerializerMethodField(method_name='get_author')

    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'status',
                  'author'
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
        return obj.author.username
