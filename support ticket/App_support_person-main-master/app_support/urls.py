from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_support import views
  
urlpatterns = [
    
    # urls partials web
    path('', views.create_subject, name="create_subject"),
    path('save_customer/',views.save_customer,name='save_customer'),
    path('save_campany/',views.save_campany,name='save_campany'),
    path('save_subject/',views.save_subject,name='save_subject'),
    
    
    path('create_customer', views.create_customer, name="create_customer"),
    path('create_customer', views.create_campany, name="create_campany"),
    
    # urls partials api
    path('customer/', views.CustomerList.as_view()),
    path('campany/', views.CampanyList.as_view()),
    path('subject/', views.SubjectList.as_view()),
    
]