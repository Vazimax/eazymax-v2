from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('about_us/',about_us,name="about"),
    path('membership/',membership,name="membership"),
    path('order_done/',order_done,name="order_done"),

    path('jobs/',jobs,name="jobs"),
    path('post_job/',post_job,name="post_job"),
    path('post/<str:pk>/',post_detail, name='post-detail'),
    path('post/<int:pk>/update/',UpdatePost,name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post-delete'),

    path('plumber/',plumber,name="plumber"),
    path('electrician/',electrician,name="electrician"),
    path('dishwasher/',dishwasher,name="dishwasher"),
    path('carpenter/',carpenter,name="carpenter"),
    path('painter/',painter,name="painter"),

]