from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# adicionar o include para importar urls dos apps
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('painel_controle.urls')),
    path('', include('painel_cantina.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
