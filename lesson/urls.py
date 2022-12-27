
from django.contrib import admin
from django.urls import path, include
from course import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v-1.0/', include(router.urls)),
    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('api/mentor/', views.MentorCreateListViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('api/mentor/<int:pk>/', views.MentorViewSet.as_view({
        'get': 'retrieve',
        'pu': 'update',
        'delete': 'destroy',

    }))
]
