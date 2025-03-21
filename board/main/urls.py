from django.urls.conf import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/main/statistics/', views.admin_statistics, name='admin_statistics'),
    path('adverts/', views.AdvertListView.as_view(), name='adverts'),
    path('adverts/<int:advert_id>', views.AdvertDetailView.as_view(), name='advert_detail'),
]
