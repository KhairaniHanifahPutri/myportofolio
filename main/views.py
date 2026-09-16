from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import AwardsForm
from main.models import Awards, Experience


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


def create_award(request):
    form = AwardsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Khairani Hanifah Putri",
        "form": form,
    }
    return render(request, "awards_form.html", context)


def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Awards.objects.all()

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize("json", awards)
    return HttpResponse(awards_json, content_type="application/json")


def show_awards(request):
    json_response = get_awards_json(request)

    awards = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards = [award.object for award in awards]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Khairani Hanifah Putri",
        "awards_list": awards,
        "title_query": title_query,
    }
    return render(request, "awards.html", context)


def delete_award(request, award_id):
    award = get_object_or_404(Awards, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")