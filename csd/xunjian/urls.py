from django.urls import path
from django.conf.urls import url
from . import views
from xunjian.views import XunjianList

urlpatterns = [
    url('list/', XunjianList, name='xunjian_list'),
    # path('ado/', views.xunjian_view, name='xunjian'),
    url('check/', views.xunjian_view, name='checking')
]