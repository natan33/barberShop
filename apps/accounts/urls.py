from django.urls import path

from apps.accounts.forms import CustomSetPasswordForm
from .views import login_view, logout_view, profile_view,register_view
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("perfil/", profile_view, name="profile"),
    path('registrar/', register_view, name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html",
        email_template_name="accounts/password_reset_email.html",
        subject_template_name='accounts/password_reset_subject.txt',
        success_url="/auth/reset_password_sent/"
    ), name="reset_password"),

    # 2. Mensagem de confirmação que o e-mail foi enviado
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_sent.html"
    ), name="password_reset_done"),

    # 3. Link com o token recebido no e-mail
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        form_class=CustomSetPasswordForm,
        template_name="accounts/password_reset_form.html",
        success_url="/auth/reset_password_complete/"
    ), name="password_reset_confirm"),

    # 4. Mensagem de sucesso final
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_complete"),
]
