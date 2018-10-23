from django.shortcuts import render
from .models import Tweet
from .forms import FormCreate
from django.views import generic

# Create your views here.
def index(request):
    context={
    "mensaje": "hola k ase",
    "numerico": 23,
    "arreglo": [1,2,3,4],
    "dic": {"a": 12, "b":43}
    }
    return render(request,"tweets/index.html",context)


class ListTweets(generic.ListView):
    template_name="tweets/list_tweets.html"
    model = Tweet

def list_tweets(request):
#    queryset= Tweet.objects.all()
    context = {
        "tweets": Tweet.objects.all()
    }
    return render(request, "tweets/list_tweets.html", context)


class DetailTweet(generic.DetailView):
    template_name = "tweets/detail.html"
    model = Tweet

def detail_tweet(request, id=1):
    queryset = Tweet.objects.get(id=id)
    context = {
        "tweet_object": queryset
    }
    return render(request, "tweets/detail.html", context)


class Create(generic.CreateView):
    template_name = "tweets/create.html"
    model = Tweet
    fields = ["user", "content"]
    success_url = "/list_tweets/"

def create(request):
    form = FormCreate(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
    else:
        form = FormCreate(request.POST or None)
    context = {
    "form": form
    }
    return render(request, "tweets/create.html", context)

class UpdateTweet(generic.UpdateView):
    template_name = "tweets/update.html"
    model = Tweet
    fields = ["content"]
    success_url = "/list_tweets/"

class DeleteTweet(generic.DeleteView):
    template_name = "tweets/delete.html"
    model = Tweet
    success_url = "/list_tweets/"
