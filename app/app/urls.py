from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('main.urls')),
    path('materials/', include('materials.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
