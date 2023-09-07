from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:exam_ref_id>', views.detail_page, name='exam'),
    path('<str:exam_ref_id>/page/<str:page>', views.pages, name='pages'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
