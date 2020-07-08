# Generated by Django 3.0 on 2020-07-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(max_length=255, upload_to='banner', verbose_name='轮播图图片')),
                ('title', models.CharField(max_length=200, verbose_name='轮播图标题')),
                ('link', models.CharField(max_length=300, verbose_name='图片链接')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示图片')),
                ('orders', models.IntegerField(default=1, verbose_name='图片排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'bz_banner',
            },
        ),
    ]
