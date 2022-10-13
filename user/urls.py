from django.urls import path
from user.views import logout_user_view, page_user_view, RegisterUser, LoginUser


urlpatterns = [
    path('log_in/', LoginUser.as_view(), name="log_in"),
    path('signin/', RegisterUser.as_view(), name='sign_in'),
    path('logout/', logout_user_view, name='log_out'),
    path('<int:user_id>/', page_user_view, name='page_user'),
]
