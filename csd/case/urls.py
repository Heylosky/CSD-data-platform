from django.urls import path

from . import views

urlpatterns = [
    path('', views.ticket_list_view.as_view(), name='ticket_list'),
    path('add/', views.ticket_create_view, name='ticket_add'),
    path('<int:pk>/', views.ticket_update_view, name='ticket_change'),
    path('ajax/load-rfos/', views.load_tickets, name='ajax_load_rfos'), # AJAX
]