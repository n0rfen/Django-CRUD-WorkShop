from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView,\
    DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from models import Post

# Create your views here.


class PostListing(ListView):
    model = Post
    paginate_by = 2
    #template_name = 'post/index.html'
    # content_object_name = 'object_list'

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'body']
	success_url = reverse_lazy('post:list')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse(
            'post:detail',
            kwargs={
                'pk': self.object.pk,
            }
        )


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')

    