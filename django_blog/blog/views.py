from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect

# Create your views here.
def blog_list(request):
    post=Post.objects.all()
    context={
        'blog_list':post
    }
    print(post)
    return render(request,'blog/blog_list.html',context)
    
def blog_details(request,id):
    postDetail=Post.objects.get(id=id)
    context={
        'blogDetail':postDetail
    }
    return render(request,'blog/blog_details.html',context)
    
def blog_delete(request,id):
    deletePost=Post.objects.get(id=id)
    deletePost.delete()
    return HttpResponseRedirect('/posts/')