from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cadastroCanetas.urls'))
    #nome do app e o arquivo url
]
