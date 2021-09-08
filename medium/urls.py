from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')


schema_view = get_schema_view(
   openapi.Info(
	  title="Product Review Backend",
	  default_version='v1',
	  description="A product review backend based on django rest framework, complete with image uploading, filtersets, and auth system with JWT and swagger UI documentation.",
	  terms_of_service="https://www.outapp.com/policies/terms/",
	  license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
	path('admin/', admin.site.urls),
	path('auth/', include('auth.urls')),
	path('', include(router.urls)),

	path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)