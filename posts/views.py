from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm


def post_create(request):
    form  = PostCreateForm()
    errors = None

    if request.method == "POST":
        form = PostCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        if form.errors:
            errors = form.errors

    template_name = 'posts/post_create.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)



def post_list(request):
    template_name = 'posts/post_list.html'
    queryset = Post.objects.all()
    context = {
        "posts": queryset,
    }
    return render(request, template_name, context)


#apis
# from django.shortcuts import render
#
# from rest_framework import generics
#
# from .models import Post
# from .serializers import PostSerializer
#
#
#
# class PostCreate(generics.CreateAPIView):
# 	serializer_class = PostSerializer
#
# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

###############################################################

