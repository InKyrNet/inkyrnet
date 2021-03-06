from django.urls import path
from magazine.views import *

app_name = 'magazine'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>-<slug:slug>', ArticleDetailView.as_view()),
    path('companies/', CompanyListView.as_view(), name='companies'),
]
