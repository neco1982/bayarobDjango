from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import index, about, contact, otomasyon, blog, otomasyon_detail, search, category_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('', index, name='index'),
    path('about/', about),
    path('contact/', contact, name='contact'),
    path('otomasyon/', otomasyon, name='otomasyon'),
    path('blog/', blog),
    path('search/', search, name='search'),
    #path('create/', post_create, name='post-create'),
    path('otomasyon/<slug>/', otomasyon_detail, name='product-detail'), 
    path('category/<cats>/', category_detail, name='category'),   
    #path('post/<id>/update/', post_update, name='post-update'),
    #path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    #path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

