# Generated by Django 4.0.1 on 2022-09-02 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('1', 'MALE'), ('2', 'FEMALE'), ('3', 'TRANSGENDER')], max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('purpose', models.CharField(choices=[('1', 'for enquiry'), ('2', 'place order'), ('3', 'return'), ('4', 'cancel')], max_length=30)),
                ('materials_provided', models.CharField(max_length=30)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeapp.course')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeapp.department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.department'),
        ),
    ]