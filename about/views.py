from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Todo


class TodoListView(ListView):
    model = Todo
    paginate_by = 3
    template_name = "about/about.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "content"]
    success_url = "/about"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = "/about"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
