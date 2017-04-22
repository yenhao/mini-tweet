from rest_framework import serializers

from tweets.models import Tweet #from ..models import Tweet

from accounts.api.serializers import UserDisplaySerializer

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_only
    class Meta:
        model = Tweet
        fields = [
            "user",
            "content"
        ]