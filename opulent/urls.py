"""opulent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from Pages.views import index1, index2 , index3, index4, index5, index6

from opulent import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', index1, name='complete-step'),
    path('2/', index2, name='complete-step'),
    path('3/', index3, name='complete-step'),
    path('4/', index4, name='complete-step'),
    path('5/', index5, name='complete-step'),
    path('6/', index6, name='complete-step'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
