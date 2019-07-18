from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.
from django.utils.safestring import mark_safe


class Credentials(models.Model):
    company_code = models.CharField(max_length=255, null=False)
    company_name = models.CharField(max_length=255, null=False)
    server_name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    server_windows_authentication = models.CharField(max_length=255, null=False)
    licence_key = models.CharField(max_length=255, null=True, blank=True)
    activate_day = models.DateField(max_length=255, null=True, blank=True)
    expire_day = models.DateField(max_length=255, null=True, blank=True)
    allowed_users = models.IntegerField(max_length=255, null=True, blank=True)
    installed_users = models.IntegerField(max_length=255, null=True, blank=True)
    windows_username = models.CharField(max_length=255, null=True, blank=True)
    windows_password = models.CharField(max_length=255, null=True, blank=True)
    company_phone = models.IntegerField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('company_code',)

    def __str__(self):
        return "{} {}".format(self.company_code, self.company_name)


class Bug(models.Model):
    compnay = models.CharField(max_length=255, null=False)
    user = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    version_of_module_software = models.CharField(max_length=255, null=True, blank=True)
    solution_description = models.CharField(max_length=255, null=False)
    solved = models.BooleanField(max_length=255, null=False)
    who_is_solving_it = models.CharField(max_length=255, null=True, blank=True)
    release_on_beta = models.BooleanField(max_length=255, null=False)
    release_on_official = models.BooleanField(max_length=255, null=False)
    database_version = models.CharField(max_length=255, null=False)
    software_version = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='images/',null=True, blank=True )
    date_entered = models.DateField(max_length=255, null=False)
    date_solved = models.DateField(max_length=255, null=False)

    class Meta:
        ordering = ('solved', 'date_entered')

    def __str__(self):
        if self.solved:
            return "{} {} {}".format(self.compnay, self.description, 'solved')
        else:
            return "{} {} {}".format(self.compnay, self.description, 'open')


class BugAdmin(admin.ModelAdmin):
    search_fields = ('compnay', 'user', 'description','version_of_module_software',)
    readonly_fields = ["show_image"]

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )


class CredentialsAdmin(admin.ModelAdmin):
    search_fields = ('company_code', 'company_name', 'server_name',)




