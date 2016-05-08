from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def blog_home(request):
	return HttpResponse("<h1>Home</h1>")


def blog_create(request):
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		print form.cleaned_data.get('title')
		instance.save()
		messages.success(request, "Succesfully Created",extra_tags = "some-other-tags")
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {
		"form":form


	}
	#return HttpResponse("<h1>Create</h1>")
	return render(request,"blog_form.html",context)

def blog_detail(request,id):
	#return HttpResponse("<h1>detail</h1>")
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id =id)
	context = {
		"title":"Details",
		"instance":instance

	}
	return render(request,"blog_detail.html",context)

	
def blog_list(request):
	#return HttpResponse("<h1>list</h1>")
	queryset = Post.objects.all().order_by("-timestamp")
	#if request.user.is_authenticated():
	context = {
		"title":"Blog Content",
		"object_list":queryset


			   }
	
	return render(request,"blog_list.html",context)


def blog_update(request,id=None):
	#return HttpResponse("<h1>Update</h1>")
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a>Saved",extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {

		"title": instance.title,
		"instance": instance,
		"form":form,

	}
	return render(request,"blog_form.html",context)

def blog_delete(request,id=None):
	
	instance=get_object_or_404(Post, id=id)
	instance.delete() 
	messages.success(request, "Successfully Deleted")
	#return HttpResponse("<h1>Delete</h1>")
	return redirect("blog:list")

