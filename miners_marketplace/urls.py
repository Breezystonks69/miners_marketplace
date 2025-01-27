from django.contrib import admin
from django.urls import path, include  # Import 'include'
from marketplace import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views  # Import auth_views for LoginView and LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list-miner/', views.list_miner, name='list_miner'),
    path('miner/<int:miner_id>/', views.miner_detail, name='miner_detail'),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
    path('accounts/login/', LoginView.as_view(template_name='marketplace/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



