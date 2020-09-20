"""Retail_data_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InventoryManagement import views as productsviews
from InventoryManagement import views as categoriesviews
from OrdersAndPayment import views as paymentsviews
from OrdersAndPayment import views as ordersviews
from OrdersAndPayment import views as orderdetailsviews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',productsviews.showProducts),
    path('Categories/',categoriesviews.showCategories),
    path('payments/', paymentsviews.showPayments),
    path('orders/', ordersviews.showOrders),
    path('orderdetails/', orderdetailsviews.showOrderDetails)


]
