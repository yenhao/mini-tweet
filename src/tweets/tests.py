from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
from .models import Tweet

User = get_user_model()

class TweetModelTestaCase(TestCase):
    def setUp(self):
        Random_user = User.objects.create(username='EricHuang')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
                user = User.objects.first(),
                content = 'Test Case - Tweeting'
            )
        self.assertTrue(obj.content == 'Test Case - Tweeting')
        self.assertTrue(obj.id == 1)
        absolute_url = reverse('tweet:detail', kwargs={'pk':1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_url(self):
        obj = Tweet.objects.create(
                user = User.objects.first(),
                content = 'Test Case - Tweeting'
            )
        absolute_url = reverse('tweet:detail', kwargs={'pk':obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)