# Generated by Django 3.2.5 on 2022-08-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nome')),
                ('price', models.FloatField(verbose_name='preço')),
                ('unit', models.IntegerField(verbose_name='unidade')),
                ('priority', models.CharField(choices=[('1', 'A'), ('2', 'B')], max_length=20, verbose_name='prioridade')),
                ('image_b64', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]