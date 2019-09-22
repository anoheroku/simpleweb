from django.urls import path

from authapp.views import WebUserLoginView, WebUserLogoutView

app_name = 'authapp'


urlpatterns = [
    path('login/', WebUserLoginView.as_view(), name='login'),
    path('logout/', WebUserLogoutView.as_view(), name='logout'),
]
