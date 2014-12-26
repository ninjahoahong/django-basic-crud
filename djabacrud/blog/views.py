from django.shortcuts import render
from blog.forms import PostForm
from blog.models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    return render_to_response("index.html", {'posts': posts},
                              context_instance=RequestContext(request))


def post_new(request):
    redirect_url = "/"
    if not request.method == "POST":
        form = PostForm()
        return render_to_response("post/post_create.html", {"form": form},
                                  context_instance=RequestContext(request))
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_url)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render_to_response("post/post.html", {'post': post},
                              context_instance=RequestContext(request))


def post_delete(request, post_id):
    redirect_url = "/"
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(redirect_url)
