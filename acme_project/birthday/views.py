from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'   

class BirthdayUpdateView(BirthdayFormMixin, BirthdayMixin, UpdateView):
    pass


class BirthdayCreateView(BirthdayFormMixin, BirthdayMixin, CreateView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


class BirthdayDetailView(DetailView):
    model = Birthday