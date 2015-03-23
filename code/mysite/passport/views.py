# coding=utf-8
import urlparse
from common.log import logger
from common.mymako import render_mako_context, render_json

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from passport.forms import AuthenticationForm, RegistrationForm


def login(request, template_name='passport/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]
    
            # Use default setting if redirect_to is empty
            if not redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL
    
            # Security check -- don't allow redirection to a different
            # host.
            elif netloc and netloc != request.get_host():
                redirect_to = settings.LOGIN_REDIRECT_URL
    
            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())
    
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
    
            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    if form.errors:
        print type(form.errors)
        print dir(form.errors)
        print form.errors.viewkeys()
        print form.errors.viewitems()
        print form.errors.values()
    context = {
        'form': form,
        redirect_field_name: redirect_to,
    }
    return render_mako_context(request, '/passport/login.html', context)

def logout(request, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Logs out the user. Redirect to the home page if not define the next page
    """
    auth_logout(request)
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if redirect_to:
        netloc = urlparse.urlparse(redirect_to)[1]
        # Security check -- don't allow redirection to a different host.
        if not (netloc and netloc != request.get_host()):
            return HttpResponseRedirect(redirect_to)
        
    redirect_to = settings.LOGIN_REDIRECT_URL
    return HttpResponseRedirect(redirect_to)


def register(request, template_name='passport/register.html',
             authentication_form=RegistrationForm):
    """
    Displays the registration page and handles the registration action.
    """
    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            # Okay, validation checks complete. Register the user.
            form.register_user()
            return render_mako_context(request, '/passport/success_register.html', {})
    else:
        form = authentication_form()

    context = {
        'form': form,
    }    
    return render_mako_context(request, '/passport/register.html', context)

