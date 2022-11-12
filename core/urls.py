from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from mecanic.views import *


urlpatterns = [
    #admin
    path('',include('account.urls')),
    path('admin/', admin.site.urls),
    #home page
    path('',index,name='home'),
    #invertory
    path("envarter/",include('inventory.urls')),
    #orders
    path("is_emirleri/",include('orders.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
