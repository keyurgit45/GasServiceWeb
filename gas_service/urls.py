"""
URL configuration for gas_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from customer_support.views import home, signup, submit_request, view_request, view_requests, support_dashboard, handle_request, delete_request

urlpatterns = [
    # home route
    path('', home, name='home'),
    # Authentication
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    # Customer routes
    path('submit/', submit_request, name='submit_request'),
    path('view_requests/', view_requests, name='view_requests'),
    path('request/<int:id>/', view_request, name='view_request'),
    path('request/delete/<int:request_id>/', delete_request, name='delete_request'),
    # Support Staff routes
    path('support/dashboard/', support_dashboard, name='support_dashboard'),
    path('support/handle_request/<int:request_id>/', handle_request, name='handle_request'),
]