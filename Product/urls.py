from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', views.categoriesViewSet)
router.register(r'product', views.prodductViewSet)




urlpatterns=router.urls



