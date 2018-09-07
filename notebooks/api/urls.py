from django.contrib import admin
from django.urls import path, include
from notebooks.api.views import NotebookPostRUDView, NotebookGetAllView

urlpatterns = [
    path('<int:pk>', NotebookPostRUDView.as_view(), name='post-rud'),
    path('', NotebookGetAllView.as_view(), name='get-all')
]