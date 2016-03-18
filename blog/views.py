from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
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
    template_name = 'blog/form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.author = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)

comment_new = login_required(CommentCreateView.as_view())


comment_edit = login_required(UpdateView.as_view(model=Comment, form_class=CommentForm, template_name='blog/form.html'))

comment_delete = login_required(DeleteView.as_view(model=Comment, success_url=reverse_lazy('blog:post_list')))






