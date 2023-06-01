from django.urls import path
from accounts.views import logout_view, register_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='form.html',
                                                redirect_authenticated_user=True,
                                                extra_context={'title': 'Login'}), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    ]