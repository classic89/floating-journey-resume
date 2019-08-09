from django.urls import path, include
from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter() 
router.register(r'myresume', views.ResumeView, 'myresume')

urlpatterns = [
#     path('', views.index, name='index'),
  path('admin/', admin.site.urls),
  path('api/', include(router.urls))
]