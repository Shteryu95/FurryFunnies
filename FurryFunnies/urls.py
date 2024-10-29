from django.contrib import admin
from django.urls import path, include

from authors.views import HomePage, Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('author/', include('authors.urls')),
    path('posts/', include('posts.urls'))
]
