from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 1
# Create your views here.
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] #어떤 필드를 입력받을지 설정
    success_url = reverse_lazy('list') #글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'
class BookmarkDetailView(DetailView):
    model = Bookmark
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
