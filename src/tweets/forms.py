from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label = '', widget = forms.Textarea(
                    attrs = {'placeholder':'Tweets something!',
                             'class': 'form-control', 
                             }
                            ))
    class Meta:
        model = Tweet
        fields = [
            # "user",
            "content"
        ]
        # exclude = ['user']
    # Validation 
    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == '\'or1=1':
    #         raise forms.ValidationError("Sql injection")
    #     return content