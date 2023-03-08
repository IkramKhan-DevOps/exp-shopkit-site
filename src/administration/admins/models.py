from django.db import models

from src.accounts.models import User


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
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.name


class ApplicationRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    software_id = models.CharField(
        unique=True, max_length=1000,
        help_text="Application ID/Client ID assigned by application activator."
    )

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Registrations"

    def __str__(self):
        return f'{self.user.username} registered {self.application.name} v{self.application.version} on {self.created_on}'


class DemoRequest(models.Model):

    STATUS_CHOICE = (
        ('pen', 'Pending'),
        ('acc', 'Accepted'),
        ('can', 'Cancelled'),
        ('mis', 'Missed'),
        ('com', 'Completed'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    time_slot = models.DateTimeField(help_text="Select demo time from [mon-sat] between [9am-5pm].")

    status = models.CharField(max_length=3, default='pe', choices=STATUS_CHOICE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Demo Requests"

    def __str__(self):
        return f'{self.name}'


class ComplainRequest(models.Model):
    STATUS_CHOICE = (
        ('pen', 'Pending'),
        ('acc', 'Accepted'),
        ('can', 'Cancelled'),
        ('res', 'Resolved'),
        ('unr', 'Un Resolved'),
    )

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    heading = models.CharField(max_length=255)
    description = models.TextField(help_text="Explain issue/bug in detail")

    status = models.CharField(max_length=3, default='pe', choices=STATUS_CHOICE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Complain Requests"

    def __str__(self):
        return f'{self.heading} filed by {self.name}'
