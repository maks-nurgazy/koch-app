from django.db import models


class AboutUs(models.Model):
    text = models.CharField(max_length=20000)

    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"

    def __str__(self):
        return self.text


class PrivacyText(models.Model):
    text = models.CharField(max_length=20000)

    class Meta:
        verbose_name = "Privacy text"
        verbose_name_plural = "Privacy text"

    def __str__(self):
        return self.text
