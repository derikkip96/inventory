from django.contrib.auth import  authenticate, login
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import redirect

# class bassed
from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME,logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
# Create your views here.

class LoginView(FormView):
    success_url = '/'
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'account/login.html'
    redirect_url = '/login/'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(self.request, username=form.cleaned_data['username'],
                            password=form.cleaned_data['password']
                            )
        if user is not None:
            if user.is_active:
                login(self.request,user)
                if self.request.session.test_cookie_worked():
                    self.request.session.delete_test_cookie()
            else:
                messages.warning(self.request, 'your account is disabled')
                return redirect('/login')
        else:
            messages.warning(self.request, 'incorrect username or password')
            return redirect('/login')
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        # redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        # if not is_safe_url(url=redirect_to, host=self.request.get_host()):
        #     redirect_to = self.success_url
        return self.success_url


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login/'
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
