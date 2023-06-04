from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.utils import json


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, HttpResponse):
            # Handle HttpResponse objects
            content = data.content
            content = content.decode('utf-8')
            data = {'body': json.loads(content)}
            return super(CustomRenderer, self).render(data, accepted_media_type, renderer_context)
        else:
            # Handle other data types
            data = {'body': data}
            return super(CustomRenderer, self).render(data, accepted_media_type, renderer_context)
