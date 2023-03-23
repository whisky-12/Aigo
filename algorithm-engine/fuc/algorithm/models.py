from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from common.utils.models import CoreModel, table_prefix

STATUS_CHOICES = (
    (0, "禁用"),
    (1, "启用"),
)


class Users(CoreModel, AbstractBaseUser, PermissionsMixin):
    """
    这里不继承AbstractUser，直接继承AbstractBaseUser和PermissionsMixin更加灵活（目前作为Open API无需用户）
    """
    username_validator = UnicodeUsernameValidator()

    # 这里用户名用UUID，然后具体的账户名用t_login表去实现
    username = models.CharField(max_length=36, unique=True, db_index=True, verbose_name="用户名",
                                help_text="用户名")
    password = None
    email = models.EmailField(max_length=128, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def set_password(self, raw_password):
        pass

    def check_password(self, raw_password):
        pass

    class Meta:
        db_table = table_prefix + "users"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)

