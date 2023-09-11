import django_filters
from django_filters import FilterSet
from .models import Post
from django.forms import widgets
class PostFilter(FilterSet):
    time = django_filters.DateFilter(lookup_expr='date__gte',widget=widgets.DateInput(attrs={"type":"date"}))



    class Meta:
       model = Post

       fields = {
           # поиск по названию
           'header': ['icontains'],
           'author':['exact'],
       }