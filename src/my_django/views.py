from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):

	my_title="Wellcome To My World"
	qs=BlogPost.objects.all()[:6]
	context={"title":my_title, 'blog_list':qs}
	
	return render(request,"home.html",context)
	## http://127.0.0.1:8000/  this is home ##


def about_page(request):
	return render(request,"about.html",{"title":"This is Akash"})


def contact_page(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form =ContactForm()
	context={ "title":"contat us ", "form":form}

	return render(request,"form.html",context)

def project_page(request):
	return render(request,"Test_page.html",{"title": "This is My Life's Work"})


def test_page(request):

	my_title="This is test...."
	return render(request,"Test_page.html",{"title":my_title})

