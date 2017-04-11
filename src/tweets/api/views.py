from django.db.models import Q
from rest_framework import generics

from tweets.models import Tweet
from .serializers import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    # queryset = Tweet.objects.all()

    # def get_queryset(self): # basic
    #     # return self.queryset
    #     return Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET.get('q'))
        query = self.request.GET.get('q')
        if query is not None:
            # qs = qs.filter(content__icontains = query) # basic
            qs = qs.filter(
                    Q(content__icontains = query) |
                    Q(user__username__icontains = query)
                )
        return qs