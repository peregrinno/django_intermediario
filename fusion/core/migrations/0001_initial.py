# Generated by Django 4.2.6 on 2023-10-31 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('produto', models.CharField(max_length=100, verbose_name='Produto')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni lni-vector', 'Design'), ('lni lni-pallet', 'Aquarela'), ('lni lni-stats-up', 'Grafico'), ('lni lni-code-alt', 'Monitor'), ('lni lni-lock', 'Cadeado'), ('lni lni-code', 'Codigo')], max_length=20, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('sub_titulo', models.CharField(max_length=80, verbose_name='Sub Título')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recurso', verbose_name='Recurso')),
            ],
            options={
                'verbose_name': 'Pacote',
                'verbose_name_plural': 'Pacotes',
            },
        ),
    ]