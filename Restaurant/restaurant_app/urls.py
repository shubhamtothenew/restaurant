from django.urls import path
from .views import *

urlpatterns = [
    # path('resturant/', resturant),
    path('search/',search),
    path('dish/<int:id>', dish, name='dish'),
    path('review/<int:id>',review, name='review'),
    path('update_review/<int:pk>/<int:id>',update_review, name='update_review'),
    path('delete_review/<int:pk>/<int:id>',delete_review, name='delete_review'),
    path('all/',home),
    path('delete/<int:id>',delete),
    path('delete_resturant/<int:id>',delete_resturant, name='delete_resturant'),
    path('delete_dish/<int:pk>/<int:id>',delete_dish, name='delete_dish'),
    path('update_resturant/<int:id>',update_resturant, name='update_resturant'),
    path('update_dish/<int:id>',update_dish, name='update_dish'),
    path('update/<int:id>',update, name='update'),
    path('form',fo,)
]
