from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_song/', views.add_song, name='add_song'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', views.signup, name='signup'),
    path('records/<int:record_id>/add_photo', views.add_photo, name='add_photo'),
]