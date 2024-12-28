from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by("-update_date")[:5]
    output = ", ".join([p.title for p in latest_post_list])
    return HttpResponse(output)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)
