from django.urls import path
from . import views

app_name = 'customer_app'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('list/', views.CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

]
