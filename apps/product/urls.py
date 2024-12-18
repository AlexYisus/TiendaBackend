from django.urls import path

from .views import ProductDetailView, ListProductsView, ListSearchView, ListRelatedView, ListBySearchView, download_pdf
from . import views
app_name="product"
urlpatterns = [
    path('product/<productId>', ProductDetailView.as_view()),
    path('get-products', ListProductsView.as_view()),
    path('search', ListSearchView.as_view()),
    path('related/<productId>', ListRelatedView.as_view()),
    path('by/search', ListBySearchView.as_view()),
    path('download-pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    ] 