"""PersonalAccounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from Main.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('home/', home, name='home'),
                  path('logout/', log_out, name='logout'),
                  path('register/', register, name="register"),
                  path('registerAccount/', createAccount, name="add-account"),
                  path('accounts/', allAccounts, name="all-account"),
                  path('accounts/edit/<int:id>', editAccount, name="edit-account"),
                  path('accounts/del/<int:id>', deleteAccount, name="delete-account"),
                  path('accounts/reset', resetAccounts, name="reset-account"),
                  path('entry/delete/<int:id>', deleteEntry, name="delete-entry"),
                  path('account/<int:id>', accountDetails, name="account-details"),
                  path('profile/<str:username>', profile, name="profile"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
