"""django_lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from lms import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('category/<int:category_id>/', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:page>/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course, name='course'),
    path('products/', views.products, name='products'),
    path('products/<int:page>/', views.products, name='products'),
    path('product/<int:product_id>/', views.product, name='product'),

    path('search/', views.search, name='search'),

    path('enrollments/', views.enrollments, name='enrollments'),
    path('enrollment/<int:enrollment_id>/', views.enrollment, name='enrollment'),
    # path('enrollment/<int:enrollment_id>/content/<int:content_id>/', views.enrollment_content, name='enrollment_content'),

    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('profile/', views.profile, name='profile'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('charge/', views.charge, name='charge'),
    path('receipt/', views.receipt, name='receipt'),
    
    path('admin/', admin.site.urls),
]
