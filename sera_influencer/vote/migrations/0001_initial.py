# Generated by Django 5.2.4 on 2025-07-19 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('pilates', '🧘\u200d♀️ 필라테스 기초 동작'), ('rehabilitation', '🏥 재활 운동 루틴'), ('stretching', '🤸\u200d♀️ 스트레칭 가이드'), ('nutrition', '🥗 운동 영양학')], max_length=20, unique=True, verbose_name='컨텐츠 타입')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('vote_count', models.PositiveIntegerField(default=0, verbose_name='투표 수')),
            ],
            options={
                'verbose_name': '투표 선택지',
                'verbose_name_plural': '투표 선택지들',
                'ordering': ['-vote_count'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='투표일자')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.voteoption', verbose_name='선택한 옵션')),
            ],
            options={
                'verbose_name': '투표',
                'verbose_name_plural': '투표들',
                'ordering': ['-created_at'],
                'unique_together': {('user', 'option')},
            },
        ),
    ]
