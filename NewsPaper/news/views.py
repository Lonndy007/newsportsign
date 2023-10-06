from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Post,Category
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
class Postivew(ListView):
    model = Post
    ordering = 'header'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news'


class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.position = self.request.path
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class PostAuth(LoginRequiredMixin, TemplateView):
    template_name = 'news_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')

class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_PostCreate','news.change_PostUpdate',
                           'news.view_PostView','news.delete_PostDelete')


class CategoryList(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.name_of_category = get_object_or_404(Category,id=self.kwargs['pk'])
        queryset = Post.objects.filter(post_category=self.name_of_category).order_by('time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.name_of_category.subscribers.all()
        context['category'] = self.name_of_category
        return context


@login_required
def subscribe(request,pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'Вы подписались на категорию!'
    return render(request,'subscribe.html',{'category':category,'message':message})



