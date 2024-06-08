from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/create/form/', views.create_post_form, name='create_post_form'),
    path('post/<int:post_id>/update/', views.update_post_form_page, name='update_post_form_page'),
    path('post/<int:post_id>/update/submit/', views.update_post_form, name='update_post_form'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
