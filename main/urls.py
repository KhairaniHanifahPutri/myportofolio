from django.urls import path

from main.views import (
    create_award_ajax,
    create_experience,
    create_experience_ajax,
    delete_experience,
    get_awards_json,
    delete_award,
    get_experience_json,
    login_user,
    logout_user,
    register,
    show_main, 
    show_experience, 
    show_awards, 
    create_award,
    toggle_star)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("awards/", show_awards, name="show_awards"),
    path("awards/add/", create_award, name="create_award"),
    path("api/awards/", get_awards_json, name="get_awards_json"),
    path("awards/<uuid:award_id>/delete/", delete_award, name="delete_award"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "experience/<uuid:experience_id>/star/", 
        toggle_star, 
        name="toggle_star",
    ),
    path(
        "awards/<uuid:award_id>/star/", 
        toggle_star, 
        name="toggle_star",
    ),
    path("awards/add-ajax/", create_award_ajax, name="create_award_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]