from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('auth/', include('auth.urls')),
	path('', include(router.urls)),
	path('openapi/', get_schema_view(
		title="Product Review Backend",
		description="A product review backend based on django rest framework, complete with image uploading, filtersets, and auth system with JWT and swagger UI documentation."
	), name='openapi-schema'),
	path('docs/', TemplateView.as_view(
		template_name='documentation.html',
		extra_context={'schema_url':'openapi-schema'}
	), name='swagger-ui'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)