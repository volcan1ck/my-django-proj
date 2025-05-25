from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.urls import re_path as url

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    #path('', views.add_task, name='add_task'),
    path('admin/', admin.site.urls),
    url(r'^books/$',views.BookListView.as_view(), name ='books'),
    path('update/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name = 'book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name = 'authors'),
]
