from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from main import api_views

app_name = "api"

urlpatterns = [
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),
    path("awards/", api_views.award_list, name="award-list"),
    path("awards/<uuid:award_id>/", api_views.award_detail, name="award-detail"),
    path("awards/<uuid:award_id>/star/", api_views.award_star, name="award-star"),
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:experience_id>/", api_views.experience_star, name="experience-star"),
]