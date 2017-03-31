from django.db import models
from django.urls import reverse
from django.conf import settings
from .validators import validate_content

# Create your models here.



class Tweet(models.Model):

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators = [validate_content])
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    # Kind of title in the admin pages
    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})

    # Build in Validation
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == '\'or1=1':
    #         raise ValidationError("Content is similar to Sql injection")
    #     return super(Tweet, self).clean(*args, **kwargs)