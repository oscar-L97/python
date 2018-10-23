from django.contrib import admin
from django.urls import path

from tweets import views

app_name="tweet"

urlpatterns = [
    path('',views.index, name="index_view"),
    path('list_tweets/', views.ListTweets.as_view(), name="list_tweets"),
    path('detail_tweet/<int:pk>/', views.DetailTweet.as_view(), name="detail_tweets"),
    path('create/',views.Create.as_view(), name="create_tweets"),
    path('update/<int:pk>', views.UpdateTweet.as_view(), name= "update_tweets"),
    path('delete/<int:pk>', views.DeleteTweet.as_view(), name = "delete_tweets"),
]
