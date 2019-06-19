from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import LoginView , LogoutView
app_name = 'account'

urlpatterns = [
    # post views
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]