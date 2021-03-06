"""trademarket_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuffs/', include('stuff.urls.stuff_urls')),
    path('categories/', include('stuff.urls.category_urls')),
    path('users/', include('user.urls.user_urls')),
    path('media/uploads/stuff_image/<str:file_name>', views.image_view),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('me/', include('user.urls.me_urls')),
    path('', views.root_view),
]
