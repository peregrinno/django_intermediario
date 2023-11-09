from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser, BaseUserManager

#SEMPRE QUE MEXER AQUI VOCÊ DEVE RODAR O COMANDO 'python manage.py makemigrations' OU VOCE VAI PERDER SUA DIGNIDADE

class UsuarioManager(BaseUserManager):
    
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)
        

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
    
class Produto(Base):
    ICONE_CHOICES = (
        ('lni lni-vector','Design'),
        ('lni lni-pallet','Aquarela'),
        ('lni lni-stats-up','Grafico'),
        ('lni lni-code-alt','Monitor'),
        ('lni lni-lock','Cadeado'),
        ('lni lni-code','Codigo'),
    )

    produto = models.CharField('Produto', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.produto
    
class Recurso(Base):
    recurso = models.CharField('Recurso', max_length=100)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso

class Pacote(Base):
    titulo = models.CharField('Título', max_length=50)
    sub_titulo = models.CharField('Sub Título',max_length=80)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    recursos = models.ManyToManyField(Recurso, verbose_name='Recursos')

    class Meta:
        verbose_name = 'Pacote'
        verbose_name_plural = 'Pacotes'

    def __str__(self):
        return self.titulo
    

    
