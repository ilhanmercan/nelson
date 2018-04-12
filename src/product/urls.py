from django.conf.urls import url

from . import views


app_name = 'product'
urlpatterns = [
    url(r'', views.ProductDetailView.as_view(), name='product'),
]
