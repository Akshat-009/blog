from django.shortcuts import render,HttpResponse
from home.models import Post,Contact
from django.contrib import messages

# Create your views here.
def index(request):
    post=Post.objects.all()
    params={'post':post}
    return render(request,"index.htm",params)
def about(request):
    return render(request,"about.htm")
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        contact=Contact(name=name, email=email, phone=phone,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,"contact.htm")
def post(request,id):
    post=Post.objects.filter(id=id)
    return render(request,"post.htm",{"post":post})
def all(request):
    post=Post.objects.all()
    params={'post':post}
    return render(request,"base.htm",params)