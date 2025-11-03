from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from noticias.views import lista_noticias


urlpatterns = [
    path('', lista_noticias, name='home'),
    path('admin/', admin.site.urls),
    path('noticias/', include('noticias.urls')),
    path('loja/', include('loja.urls')),
    path('contas/', include('contas.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('carrinho/', include('carrinho.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
