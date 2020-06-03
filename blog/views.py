from django.shortcuts import render
from .models import Post
def post_list(request):
    post=Post.objects.all()
    #context={
     #   'post_list':post
    #}
    return render(request, "blog/post_list.html",{})#context)
    

# Create your views here.
