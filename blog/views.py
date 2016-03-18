from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post


'''
def post_list(request):
    return render(request, 'blog/post_list.html')
'''


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)
