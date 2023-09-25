from django.urls import path
from .views import  Postivew,PostDetail,PostCreate,PostUpdate,PostDelete,CategoryList,subscribe


urlpatterns = [
   path('',  Postivew.as_view(),name='news'),
   path('<int:pk>', PostDetail.as_view(),name='news_detail'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('article/create/',PostCreate.as_view(),name='article_create'),
   path('article/<int:pk>/update/', PostUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
   path('categories/<int:pk>',CategoryList.as_view(),name='category_list'),
   path('categories/<int:pk>/subscribe',subscribe,name='subscribe'),
]
