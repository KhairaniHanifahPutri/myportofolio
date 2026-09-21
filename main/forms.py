from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Awards, Experience

class AwardsForm(ModelForm):
    class Meta:
        model = Awards
        fields = ['title', 'description', 'category', 'awarded_at']

        labels = {
            "title": "Nama Penghargaan",
            "description": "Deskripsi Penghargaan",
            "category": "Kategori Penghargaan",
            "awarded_at": "Tanggal Diperoleh",
        }

        widgets = {
            'title': TextInput(
                attrs={
                    "placeholder": 'Masukkan nama penghargaan',
                }
            ),
            'description': Textarea(
                attrs={
                    "placeholder": 'Masukkan deskripsi penghargaan',
                }
            ),
            'category': TextInput(
                attrs={
                    "placeholder": 'Masukkan kategori penghargaan',
                }
            ),
            'awarded_at': TextInput(
                attrs={
                    "placeholder": 'Masukkan tanggal diperoleh (format: YYYY-MM-DD)',
                }
            ),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'category', 'thumbnail']

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Thumbnail",
        }

        widgets = {
            'title': TextInput(
                attrs={
                    "placeholder": 'Masukkan nama pengalaman',
                }
            ),
            'description': Textarea(
                attrs={
                    "placeholder": 'Masukkan deskripsi pengalaman',
                }
            ),
            'category': TextInput(
                attrs={
                    "placeholder": 'Masukkan kategori pengalaman',
                }
            ),
            'thumbnail': URLInput(
                attrs={
                    "placeholder": 'Masukkan URL thumbnail (opsional)',
                }
            ),
        }
