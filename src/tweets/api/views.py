from rest_framework import generics

from tweets.models import Tweet
from .serializers import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    # queryset = Tweet.objects.all()

    def get_queryset(self):
        # return self.queryset
        return Tweet.objects.all()