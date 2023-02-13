from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('terms-of-service/', views.terms, name='terms-of-service'),
    path('hiring/pricing/', views.pricing, name='pricing'),
    path('accounts/', include('allauth.urls')),
    path('', include('candidates.urls')),
    path('hiring/', include('recruiters.urls')),
    path('', include('pwa.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="reset_password"),
    path('reset_password_set/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_send.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), name="password_reset_complete"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)