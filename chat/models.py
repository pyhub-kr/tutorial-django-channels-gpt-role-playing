# chat/models.py

from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class RolePlayingRoom(models.Model):
    class Language(models.TextChoices):
        ENGLISH = "en-US", "English"
        JAPANESE = "ja-JP", "Japanese"
        CHINESE = "zh-CN", "Chinese"
        SPANISH = "es-ES", "Spanish"
        FRENCH = "fr-FR", "French"
        GERMAN = "de-DE", "German"
        RUSSIAN = "ru-RU", "Russian"

    class Level(models.IntegerChoices):
        BEGINNER = 1, "초급"
        ADVANCED = 2, "고급"

    class Meta:
        ordering = ["-pk"]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=Language.choices, default=Language.ENGLISH, verbose_name="대화 언어")
    level = models.SmallIntegerField(choices=Level.choices, default=Level.BEGINNER, verbose_name="레벨")

    situation = models.CharField(max_length=100, validators=[MinLengthValidator(3)], verbose_name="상황")
    situation_en = models.CharField(max_length=100, blank=True, verbose_name="상황 (영문)",
                                    help_text="GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.")
    my_role = models.CharField(max_length=100, verbose_name="내 역할")
    my_role_en = models.CharField(max_length=100, blank=True, verbose_name="내 역할 (영문)",
                                  help_text="GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.")
    gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할")
    gpt_role_en = models.CharField(max_length=100, blank=True, verbose_name="GPT 역할 (영문)",
                                   help_text="GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.")

    def get_absolute_url(self) -> str:
        return reverse("role_playing_room_detail", args=[self.pk])
