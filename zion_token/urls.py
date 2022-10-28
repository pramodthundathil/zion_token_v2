
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import TokenCall
from TokenCall import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(TokenCall.urls)),
]
