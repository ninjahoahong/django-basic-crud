from django.shortcuts import render
from blog.forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def post_new(request):
    redirect_url = "/admin"
    if not request.method == "POST":
        form = PostForm()
        return render_to_response("post/post_create.html", {"form": form}, context_instance=RequestContext(request))
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_url)
