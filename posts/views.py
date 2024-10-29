from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authors.models import Author
from posts.forms import CreatePost, EditPost, DeletePost
from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = 'details-post.html'
    pk_url_kwarg = 'id'


class PostEditView(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    pk_url_kwarg = 'id'
    form_class = EditPost
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    pk_url_kwarg = 'id'
    form_class = DeletePost
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
