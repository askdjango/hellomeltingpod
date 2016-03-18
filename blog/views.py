from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm


'''
def post_list(request):
    return render(request, 'blog/post_list.html')
'''


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.author = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)

comment_new = login_required(CommentCreateView.as_view())








