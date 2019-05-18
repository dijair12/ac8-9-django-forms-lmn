"""lmsimpacta URL Configuration

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
from django.urls import include, path

from contas.urls import CONTAS_URLS
from cursos.urls import CURSOS_URLS
from restrito.urls import RESTRITO_URLS
from website.urls import WEBSITE_URLS

urlpatterns = [
    path('contas/', include(CONTAS_URLS)),
    path('cursos/', include(CURSOS_URLS)),
    path('restrito/', include(RESTRITO_URLS)),
    path('', include(WEBSITE_URLS)),
]
