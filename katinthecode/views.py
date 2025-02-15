"""This is the views file for the katinthecode app."""

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def index(request):
    """This is the index view for the katinthecode app."""
    latest_post_list = Post.objects.order_by("-update_date")[:5]
    output = ", ".join([p.title for p in latest_post_list])
    return HttpResponse(output)


def detail(request, post_id):
    """This is the detail view for the katinthecode app."""
    return HttpResponse(f"You're looking at post {post_id}s.")
