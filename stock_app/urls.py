from django.urls import include, path

urlpatterns = [
    path('', include('stock_viewer.urls')),
]