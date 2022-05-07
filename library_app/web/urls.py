from django.urls import path

from library_app.web.views import show_index, create_book, edit_book, show_book_details, show_profile, edit_profile, \
    delete_profile, create_profile

urlpatterns = [
    path('', show_index, name='show index'),
    path('add/', create_book, name='create book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', show_book_details, name='show book details'),
    # path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/create/', create_profile, name='create profile'),
]
