from django.urls import path, include

from authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='create-author'),
    path('details/', views.AuthorDetailsView.as_view(), name='author-details'),
    path('edit/', views.AuthorEditView.as_view(), name='edit-author'),
    path('delete/', views.AuthorDeleteView.as_view(), name='delete-author'),
]