from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ContactViewSet, OpportunityViewSet, InteractionViewSet
from . import views


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'opportunities', OpportunityViewSet)
router.register(r'interactions', InteractionViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/new/', views.customer_create, name='customer_create'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunity/new/', views.opportunity_create, name='opportunity_create'),
    path('opportunity/<int:pk>/', views.opportunity_detail, name='opportunity_detail'),
    path('opportunity/<int:pk>/edit/', views.opportunity_edit, name='opportunity_edit'),
    path('opportunity/<int:pk>/delete/', views.opportunity_delete, name='opportunity_delete'),
    path('interactions/', views.interaction_list, name='interaction_list'),  
    path('interaction/add/', views.interaction_create, name='interaction_create'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),  # Define detail view URL
    path('contacts/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('api/', include(router.urls)),
]