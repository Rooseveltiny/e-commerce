from django.urls import path
from . import views

# app_name = 'db_orm'

urlpatterns = [
    path('load_data/', views.load_data, name='load_data'),
    path('main/', views.main_page, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('mogo/', views.get_mogo, name='mogo'),
]