from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class WebUserLoginView(LoginView):
    template_name = 'authapp/login.html'
    success_url = reverse_lazy('admin:index')

    def get_success_url(self):
        return self.success_url


class WebUserLogoutView(LogoutView):
    template_name = 'authapp/logout.html'
    success_url = reverse_lazy('webapp:root')
