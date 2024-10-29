from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from authors.forms import CreateAuthor, EditAuthor
from authors.models import Author
from posts.models import Post


class HomePage(TemplateView):
    model = Author
    template_name = 'index.html'


class Dashboard(ListView):
    model = Post
    template_name = 'dashboard.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = CreateAuthor
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailsView(ListView):
    template_name = 'details-author.html'
    context_object_name = 'my_posts'

    def get_queryset(self):
        return Post.objects.order_by('-updated_at').first() or 'N/A'


class AuthorEditView(UpdateView):
    model = Author
    template_name = 'edit-author.html'
    form_class = EditAuthor
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return Author.objects.first()


class AuthorDeleteView(DeleteView):
    template_name = 'delete-author.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Author.objects.first()
