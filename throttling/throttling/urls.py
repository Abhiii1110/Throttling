# from django.contrib import admin
# from django.db import router
# from django.urls import include, path
# from api import views
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()


# router.register('studentapi', views.StundentModelViewSet,basename='student')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('', include('rest_framework.urls', namespace='rest_framework')),
# ]

# SCOPE THROTTLING

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>', views.StudentDestroy.as_view()),


    # path('studentapi/', views.Get_Post_student.as_view()),
    # path('studentapi/<int:pk>', views.retrive_Update_Destroy_student.as_view()),
]
