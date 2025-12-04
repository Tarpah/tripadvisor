from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms.custom_login_form import CustomLoginForm
from .views import index
from .views import UsuarioRegisterView

urlpatterns = [
    path('register/', UsuarioRegisterView.as_view(), name='register_user'),

    # rotas para logar
    path('accounts/login/', auth_views.LoginView.as_view(template_name ="accounts/login.html",
                                                               authentication_form=CustomLoginForm)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tripadvisor/', include('tripadvisor.urls'),),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]