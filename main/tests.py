from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Awards


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.award = Awards.objects.create(
            title="Juara 1 Lomba Programming",
            description="Memenangkan lomba programming tingkat nasional.",
            category="Academic",
            awarded_at="2024-01-15",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.award.title) #Test award
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_awards_model(self):
        self.assertEqual(str(self.award), "Juara 1 Lomba Programming")
        self.assertEqual(self.award.category, "Academic")
        self.assertEqual(str(self.award.awarded_at), "2024-01-15")

    def test_awards_page(self):
        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "awards.html")
        self.assertContains(response, self.award.title)
        self.assertContains(response, self.award.description)
        self.assertContains(response, "Academic")
        self.assertContains(response, "Jan. 15, 2024")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_awards_page(self):
        Awards.objects.all().delete()
        response = self.client.get(reverse("main:show_awards"))

        self.assertContains(response, "Belum ada penghargaan yang ditambahkan.")
