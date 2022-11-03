from django.urls import path
from user.views import logout_user_view, page_user_view, RegisterUser, LoginUser
from user.views import UpdateEmailView, DeleteUserView, PasswordUpdateView


urlpatterns = [
    path('log_in/', LoginUser.as_view(), name="log_in"),
    path('signin/', RegisterUser.as_view(), name='sign_in'),
    path('logout/', logout_user_view, name='log_out'),
    path('<int:user_id>/', page_user_view, name='page_user'),
    path('<int:pk>/update/', UpdateEmailView.as_view(), name="update_email"),
    path('<int:pk>/password_change/', PasswordUpdateView.as_view(), name='password_change'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
]
