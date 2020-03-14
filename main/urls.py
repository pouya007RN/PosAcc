from . import views
from django.urls import path

urlpatterns = [

                path('', views.index,name="homepage"),
                path('stock/',views.devices,name='stock'),
                path('order/',views.order,name='order'),
                path('clients/<slug>/', views.client_detail,name='det'),
                path('clients/', views.client,name='client'),
                path('costs/', views.cost,name='cost'),
                path('bank/', views.bank,name='bank'),
                path('login/', views.loginPage,name='login'),
                path('logout/', views.logout_request,name='logout'),
                path('accounts/login/', views.loginPage,name='login'),

]
