from django.shortcuts import render
from blog.models import Blog


# Create your views here.
def view_blog(request):
    return render(request, 'blog.html') 

def view_all_blogs(request):
    blogs= Blog.objects.all()
    context= {'blogs':blogs}
    return render(request, 'blogs.html', context)

def view_a_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    context = {'blog' :blog}
    return render (request, 'blog.html', context)
    
    
    
