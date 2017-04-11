from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_counts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            # "email",
            "follower_counts",
        ]
    def get_follower_counts(self, obj):
        # print(obj.username)
        return 0