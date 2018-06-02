from django.urls import include, path

from .views import post_create, post_list

urlpatterns = [
    # path('', views.PostList.as_view()),

    path('', post_list, name='post-list'),
    path('posts/create/', post_create, name='post-create'),
]