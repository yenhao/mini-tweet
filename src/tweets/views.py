from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Tweet
from .forms import TweetModelForm

# Create
class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/form.html'
    success_url = '/tweet/create/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


# Retrieve
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/detail_view.html'
    
    # def get_object(self): #pk == id
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(id = pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/list_view.html'
    


# def tweet_detail_view(request, id = 1):
#     obj = Tweet.objects.get(id = id) #Get from db
#     context = {
#         "object" : obj
#     }
#     return render(request, 'tweets/detail_view.html', context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, 'tweets/list_view.html', context)