from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='Regina',
        default_version='v1',
        description='Regina Karimova',
    )
)


urlpatterns = [
    path('', RedirectView.as_view(url='/swagger')),
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='subjects')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static('media', document_root=settings.MEDIA_ROOT)
