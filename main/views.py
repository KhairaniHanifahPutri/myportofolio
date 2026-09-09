from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Khairani Hanifah Putri",
        "npm": "2506587371",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An information system student who has an interest in human relationships. "
            "I am a passionate learner that lately focused on learning data visualization as a hobby. "
            "Still, I always look for a chance to improve my skills especially in communication and IT skills."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Khairani Hanifah Putri",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)