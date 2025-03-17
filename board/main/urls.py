from django.urls.conf import path

from . import views

urlpatterns = [
    path('admin/main/statistics/', views.admin_statistics, name='statistics'),
    path('adverts/', views.AdvertListView.as_view(), name='adverts'),
    path('adverts/<int:advert_id>', views.AdvertDetailView.as_view(), name='advert_detail'),
]
