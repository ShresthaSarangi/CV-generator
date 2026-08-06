from django.urls import path
from . import views
urlpatterns = [
    path('saveprofile/',views.save_profile,name='save-profile'),
    path('<int:id>/',views.resume,name='resume'),
    path('',views.dashboard,name='dashboard'),
    path('download/<int:id>/',views.download_resume,name='download_resume'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
]