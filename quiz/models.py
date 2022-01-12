from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError


class Quiz(models.Model):

    title = models.CharField(
        _("title"), max_length=100, blank=False, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(
        _("description"), max_length=1000, default='default desc')

    def save(self):
        if self.end_date < self.start_date:
            raise ValidationError('The end date must be after the start date.')
        super().save()

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = (('text', 'text'),
                      ('radio', 'radio'),
                      ('checkbox', 'checkbox'))

    text = models.TextField(_("text"), max_length=100)
    q_type = models.CharField(_('type'), choices=QUESTION_TYPES, max_length=8)
    quiz = models.ForeignKey(Quiz, verbose_name=_(
        "quiz"), related_name='question',  on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choice', on_delete=models.CASCADE)
    text = models.CharField(_("text"), max_length=50)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.IntegerField(verbose_name=_('user'))
    quiz = models.ForeignKey(Quiz, verbose_name=_(
        "quiz"), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name=_(
        "question"), related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(
        _("answer"), max_length=100, blank=True, null=True)
    answer_choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, blank=True, null=True)
