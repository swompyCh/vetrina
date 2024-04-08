from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.catalog, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CatalogDetailView.as_view(), name='catalog-detail'),
    path('<int:pk>/update', views.CatalogUpdateView.as_view(), name='catalog-update'),
    path('<int:pk>/delete', views.CatalogDeleteView.as_view(), name='catalog-delete'),
]
