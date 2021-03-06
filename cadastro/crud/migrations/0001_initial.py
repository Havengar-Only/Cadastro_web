# Generated by Django 4.0.5 on 2022-06-23 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullnome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.produtos')),
            ],
        ),
    ]
