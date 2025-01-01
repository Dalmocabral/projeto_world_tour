from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import pycountry
from django.contrib.auth import get_user_model



def get_country_choices():
    country_choices = [(country.alpha_2, country.name) for country in pycountry.countries]
    return country_choices


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, username_IFC, **extra_fields):
        # Verificar se o email foi fornecido
        if not email:
            raise ValueError('Email must be provided')
        # Verificar se a senha foi fornecida
        if not password:
            raise ValueError('Password must be provided')

        # Criar um novo usuário
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username_IFC=username_IFC
            **extra_fields
        )

        # Configurar a senha do usuário e salvar no banco de dados
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, username_IFC, **extra_fields):
        # Configurar as permissões padrão para um usuário normal
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, username_IFC, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, username_IFC, **extra_fields):
        # Configurar as permissões para um superusuário
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Chamar o método _create_user para criar o superusuário
        return self._create_user(email, password, first_name, last_name, username_IFC **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    # Definir os campos do modelo de usuário
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)    
    username_IFC = models.CharField(max_length=240, null=True, blank=True)    
    country = models.CharField('', max_length=2, null=True, blank=True, choices=get_country_choices(), help_text='Selecione o país')
   
    

    # Configurar as permissões do usuário
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    # Configurar o campo usado para fazer login
    USERNAME_FIELD = 'email'
    # Definir os campos obrigatórios ao criar um usuário
    REQUIRED_FIELDS = ['first_name', 'last_name']

    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'