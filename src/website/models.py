from django.db import models


class Application(models.Model):
    OPERATING_SYSTEM_CHOICE = (
        ('w', 'Windows'),
        ('l', 'Linux'),
        ('m', 'Mac'),
        ('g', 'Global'),
    )
    CATEGORY_CHOICE = (
        ('f', 'Free'),
        ('p', 'Premium')
    )

    name = models.CharField(max_length=255)
    version = models.FloatField(help_text="Application version must be update [0.*] or upgrade [*.0]")
    description = models.TextField(null=True, blank=True, help_text="Detailed down description")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICE)
    operating_system = models.CharField(max_length=1, choices=OPERATING_SYSTEM_CHOICE)
    app_file = models.FileField(upload_to='applications/', help_text="Please user a installers or zip files here")

    total_downloads = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Applications and Versions"

    def __str__(self):
        return self.name
