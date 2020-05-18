from django.urls import path, include
from .views import BlogListView, BlogDetailView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name = 'home'),
    path('<int:pk>/', BlogDetailView.as_view(), name = 'detail')
]
