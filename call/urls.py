from django.urls import path
from .views import login_view
from django.contrib import admin
from .views import dashboard_view
from .views import initiate_video_call
from .views import start_video_call
from . import views
from .views import signup
from .views import user_login_view, user_dashboard
from .views import user_management



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('initiate_video_call/', initiate_video_call, name='initiate_video_call'),
    path('start/', views.start_video_call, name='start_video_call'),
    path('start/<str:mother_id>/', views.start_video_call, name='start_video_call_with_id'),
    path('signup/', signup, name='signup'),
    path('login/', user_login_view, name='user_login'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('user-management/', user_management, name='user_management'),
    
    
]