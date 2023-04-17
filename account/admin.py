from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[RegexValidator(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', 
            _(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%).")
        )]
    )

    class Meta:
        model = User
        fields = ('email', 'alias', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'alias', 'password', 'is_deactivated', 'is_verified', 'is_active', 'is_staff', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'alias', 'date_joined','last_login', 'is_superuser', 'is_admin', 'is_staff', 'is_active', 'is_deactivated', 'is_verified')
    list_filter = ('is_admin', 'is_staff',)
    search_fields = ('email', 'alias',)
    readonly_fields = ('uid', 'date_joined','last_login')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        ('Personal info', {'fields': ('uid','email', 'alias','full_name')}),
        ('Meta', {'fields': ('date_joined','last_login')}),
        ('Private', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff','is_active', 'is_verified', 'is_deactivated')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )



# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)