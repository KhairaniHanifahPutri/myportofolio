from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini

from django.views.decorators.http import require_POST
from main.forms import AwardsForm, ExperienceForm
from main.models import Awards, Experience
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Khairani Hanifah Putri",
        "npm": "2506587371",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An information system student who has an interest in human relationships. "
            "I am a passionate learner that lately focused on learning data visualization as a hobby. "
            "Still, I always look for a chance to improve my skills especially in communication and IT skills."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Khairani Hanifah Putri",
        "form": form,
    }
    return render(request, "register.html", context)

@login_required(login_url="/login/")
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

    data = []
    for award in awards:
        starred_users = award.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(award.id),
            "fields": {
                "title": award.title,
                "description": award.description,
                "tech_stack": award.tech_stack,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


def show_awards(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Khairani Hanifah Putri",
        "title_query": title_query,
        "form": AwardsForm(),
    }
    return render(request, "awards.html", context)

@login_required(login_url="/login/")
def delete_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    award = get_object_or_404(Awards, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Khairani Hanifah Putri",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request):

    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize(
        "json", experience, use_natural_foreign_keys=True
        )
    return HttpResponse(experience_json, content_type="application/json")


def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [experience.object for experience in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Khairani Hanifah Putri",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Khairani Hanifah Putri",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")


def toggle_star(request, awards_id):
    awards = get_object_or_404(Awards, pk=awards_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in awards.starred_by.all():
            awards.starred_by.remove(request.user)
        else:
            awards.starred_by.add(request.user)

    return redirect("main:show_awards")


@require_POST
def create_award_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan penghargaan."},
            status=403,
        )

    form = AwardsForm(request.POST)
    if form.is_valid():
        award = form.save()
        return JsonResponse(
            {"message": "Penghargaan berhasil ditambahkan.", "pk": str(award.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

