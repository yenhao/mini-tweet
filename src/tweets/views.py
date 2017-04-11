from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/tweet_create.html'
    # success_url = '/tweet/create/'
    success_url = reverse_lazy("tweet:list")
    login_url = '/admin/'
    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to be continue'])
    #         return self.form_invalid(form)

#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/tweet_update.html'
    # success_url = '/tweet/'
    login_url = '/admin/'

#Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list") # reverse
    login_url = '/admin/'

# Retrieve
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/detail_view.html'
    
    # def get_object(self): #pk == id
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(id = pk) 

class TweetListView(ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            # qs = qs.filter(content__icontains = query) # basic
            qs = qs.filter(
                    Q(content__icontains = query) |
                    Q(user__username__icontains = query)
                )
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')

        return context

    


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