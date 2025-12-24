from django.db import models
from django.conf import settings
from events.models import Event


class Submission(models.Model):
   
    class SubmissionType(models.TextChoices):
        oral = 'oral', 'oral'
        poster = 'poster', 'poster'
        affiche = 'affiche', 'affiche'
                  #value for db - label for user 


    class SubmissionStatus(models.TextChoices):
        pending = 'pending', 'pending'
        accepted = 'accepted', 'accepted'
        rejected = 'rejected', 'rejected'
        revision = 'revision', 'revision'

    #  لازم تربطو مع باه يعرف لاي حدث رايح يمد خدمتو(Event)
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE,
        related_name='submissions',
        verbose_name='Event'
    )

    #  gestion du status
    title = models.CharField(max_length=50, verbose_name="Title")
    abstract = models.TextField(verbose_name="Résumé")
    keywords = models.CharField(max_length=100, verbose_name="Keywords")
    
    # tipe de soumission (oral, poster, affiche)
    sub_type = models.CharField(
        max_length=20,
        choices=SubmissionType.choices,#choises yarbt les tipes li dernahom felclasse m3a bd
        default=SubmissionType.oral,
        verbose_name='Submission Type'
    )

    #  ا(PDF)
    pdf_file = models.FileField(
        upload_to='submissions/%Y/%m/%d/', 
        verbose_name="PDF File"
    )

    #  حالة التقديم
    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.pending,
        verbose_name='Statut'
    )

    # صاحب التقديمCommunicant
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur Principal'
    )

    # كي يبعت بعد المقترح تاعو يتسجل التاريخ لي بعت فبه
    sub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
  
