from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('perguntas/', include('apps.questionario.urls', namespace='perguntas')),
]
