from django.urls import path
from blog import views


urlpatterns = [
    path('', views.list_blogs, name='blog_list'),
    path('blog/<int:pk>', views.detail_blog, name='blogs_detail'),
    path("blog/create", views.BlogCreateView.as_view(), name="blog_create"),
]
