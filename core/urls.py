from rest_framework.routers import DefaultRouter

from core import views

app_name = 'core'

router = DefaultRouter()

router.register('subjects', views.SubjectsViewSet, basename='subjects')
router.register('pupils', views.PupilViewSet, basename='pupils')

urlpatterns = router.urls
