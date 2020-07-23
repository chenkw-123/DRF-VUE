# Generated by Django 2.0.6 on 2020-07-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(max_length=255, upload_to='banner', verbose_name='轮播图片')),
                ('title', models.CharField(max_length=50, verbose_name='轮播图标题')),
                ('link', models.CharField(max_length=300, verbose_name='图片的链接')),
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
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='图片排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.BaseModel')),
                ('title', models.CharField(max_length=200, verbose_name='导航标题')),
                ('link', models.CharField(max_length=300, verbose_name='导航链接')),
                ('position', models.IntegerField(choices=[(1, '顶部导航'), (2, '底部导航')], default=1, verbose_name='导航位置')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是外部链接')),
            ],
            options={
                'verbose_name': '导航栏',
                'verbose_name_plural': '导航栏',
                'db_table': 'bz_nav',
            },
            bases=('home.basemodel',),
        ),
    ]
