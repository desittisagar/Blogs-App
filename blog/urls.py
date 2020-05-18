from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'detail'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete')
]
