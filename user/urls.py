from django.urls import path
from user.views import login_user_view, logout_user_view, page_user_view, SighInView


urlpatterns = [
    path('log_in/', login_user_view, name="log_in"),
    path('signin/', SighInView.as_view(), name='sign_in'),
    path('logout/', logout_user_view, name='log_out'),
    path('<int:user_id>/', page_user_view, name='page_user'),
]
