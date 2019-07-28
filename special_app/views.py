from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
from django.utils import timezone

from .forms import BlogPost

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})


def create(hoho):
    blog = Blog()
    blog.title = hoho.GET['title']
    blog.body = hoho.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def new(request):
    return render(request, 'new.html')

def home(haha):
    blog_list = Blog.objects.get_queryset().order_by('id')
    sliced = Paginator(blog_list,3)
    page_num = haha.GET.get('page')
    send_this = sliced.get_page(page_num)
    return render(haha, 'home.html', {'posts': send_this})


def detail(request, abc):
    blog_detail = get_object_or_404(Blog, pk = abc)
    return render(request, 'detail.html', {'a': blog_detail})


