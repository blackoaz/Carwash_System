import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_tenants.models import TenantMixin, DomainMixin
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', 'Manager')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Abstract base user has password, last_login, is_active by default
    USERTYPE_CHOICES = (
    ('Auditor', 'Auditor'), 
    ('Manager', 'Manager'),
    ('Operator', 'Operator'),
)
    username_validator = ASCIIUsernameValidator()
    
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = CICharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = CIEmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
        blank=True,
    )
    phone_number = PhoneNumberField()
    national_id_number = models.IntegerField(unique=True)
    user_type = models.CharField(max_length=30, choices=USERTYPE_CHOICES, default='Operator')
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    is_superuser = models.BooleanField(
        _("superuser"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as a superuser."
        ),
    )
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number', 'national_id_number', 'user_type']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        if self.email:
            self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
    
    
class Client(TenantMixin):
    tenant_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    tenant_uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
class Domain(DomainMixin):
    pass
