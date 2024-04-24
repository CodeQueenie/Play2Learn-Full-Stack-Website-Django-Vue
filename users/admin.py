from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

from common.admin import Play2LearnAdmin
from common.utils.admin import append_fields, move_fields, remove_fields

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):
    model = CustomUser

    # List Attributes
    list_display = UserAdmin.list_display + ("is_superuser",)
    list_display_links = ("username", "email", "first_name", "last_name")

    readonly_fields = ["password_form"]

    # Fields for editing existing user
    new_fields = ("dob", "avatar")
    # Add new fields to 'Personal info' fieldset.
    append_fields(UserAdmin.fieldsets, "Personal info", new_fields)

    # Move email field from 'Personal info' fieldset to unlabelled fieldset
    move_fields(UserAdmin.fieldsets, "Personal info", None, ("email",))

    # Remove password field.
    remove_fields(UserAdmin.fieldsets, None, ("password",))
    # Add password change form link instead
    append_fields(UserAdmin.fieldsets, None, ("password_form",))

    # Fields for adding new user.
    new_fields = ("email",)
    # Add new fields to unlabelled fieldsets.
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, None, new_fields)

    # Personal Info
    personal_info = ("first_name", "last_name", "dob")
    add_fieldsets = append_fields(
        UserAdmin.add_fieldsets, "Personal Info", personal_info
    )

    def password_form(self, obj):
        url = reverse("admin:auth_user_password_change", args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    # Add Save buttons to the top of the change user form
    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)


admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)