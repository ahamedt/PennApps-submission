from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostDeleteView, likes_view

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('like/<int:pk>/', views.likes_view,name='post-like'),

]
##Old path for detail view
##path('post/<int:pk>/', views.POST_DETAIL, name = 'post-detail'),
