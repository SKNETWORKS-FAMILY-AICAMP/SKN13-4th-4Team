# Generated manually for FeedLike model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='좋아요 날짜')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='feed.feedpost', verbose_name='포스트')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '피드 좋아요',
                'verbose_name_plural': '피드 좋아요들',
            },
        ),
        migrations.AddConstraint(
            model_name='feedlike',
            constraint=models.UniqueConstraint(fields=('post', 'user'), name='unique_post_user_like'),
        ),
    ]
