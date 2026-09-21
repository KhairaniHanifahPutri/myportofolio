from django.urls import path

from main.views import (
    create_experience,
    delete_experience,
    get_awards_json,
    delete_award,
    get_experience_json,
    show_main, 
    show_experience, 
    show_awards, 
    create_award)

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
]