from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
from django.contrib.auth import views as auth_views
from profiles import views as profiles_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('profile/<int:pk>', profiles_views.profile, name='profile'),
    path('profile/update', profiles_views.update, name='update'),

    path('password-reset/', 
            auth_views.PasswordResetView.as_view(template_name="profiles/password_reset.html"), 
            name="password_reset"),
    path('password-reset/confirm/<uidb64>/<token>', 
            auth_views.PasswordResetConfirmView.as_view(template_name="profiles/password_reset_confirm.html"), 
            name="password_reset_confirm"),
    path('password-reset/done', 
            auth_views.PasswordResetDoneView.as_view(template_name="profiles/password_reset_done.html"),
            name="password_reset_done"),
    path('password-reset/complete',
            auth_views.PasswordResetCompleteView.as_view(template_name="profiles/password_reset_complete.html"),
            name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
