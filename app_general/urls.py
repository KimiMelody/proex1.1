from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('evaluation/<str:exam_ref_id>',views.evaluation_spec,name='eva_spec'),
    path('shop/', views.shop, name='shop'),
    path('shop/<str:stortnote_id>',views.shopdetail,name='shopdetail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)