from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'flatpages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'flatpages/logout.html'), name='logout'),
    path('logout/confirm/', TemplateView.as_view(template_name = 'flatpages/logout_confirm.html'), name='logout_confirm'),
]