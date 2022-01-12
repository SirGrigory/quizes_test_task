# Generated by Django 3.2.9 on 2022-01-12 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20211228_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='answer_text',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz', verbose_name='quiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='first_quiz', max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.IntegerField(verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.CharField(choices=[('text', 'text'), ('radio', 'radio'), ('checkbox', 'checkbox')], max_length=8, verbose_name='type'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='quiz.question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.choice'),
        ),
    ]