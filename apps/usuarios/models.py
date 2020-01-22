from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, tipo_usuario, password=None):
        user = self.model(
            email=self.normalize_email(email),
            tipo_usuario=tipo_usuario,
        )

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if password:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            tipo_usuario="P",
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    TIPO_USUARIO = (
        ("P", "Porteiro"),
    )

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=254,
        unique=True,
    )

    tipo_usuario = models.CharField(
        verbose_name="Tipo de usuário",
        max_length=1,
        choices=TIPO_USUARIO,
        default="P",
    )

    is_active = models.BooleanField(
        "usuario ativo?",
        default=False
    )

    is_staff = models.BooleanField(
        "usuario é da equipe de desenvolvimento?",
        default=False
    )

    is_superuser = models.BooleanField(
        "usuario é um superusuário?",
        default=False
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name="Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email
