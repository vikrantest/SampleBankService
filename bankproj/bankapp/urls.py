from django.conf.urls import url,include
from django.contrib import admin
import bankapp.views as bankappViews

urlpatterns = [
    url(r'^/', admin.site.urls),
]
 