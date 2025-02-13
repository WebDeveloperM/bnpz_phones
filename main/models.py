from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Departament(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    nickname_1 = models.CharField(max_length=255, verbose_name='Nickname 1', null=True, blank=True)
    nickname_2 = models.CharField(max_length=255, verbose_name='Nickname 2', null=True, blank=True)
    nickname_3 = models.CharField(max_length=255, verbose_name='Nickname 3', null=True, blank=True)
    nickname_4 = models.CharField(max_length=255, verbose_name='Nickname 4', null=True, blank=True)
    nickname_5 = models.CharField(max_length=255, verbose_name='Nickname 5', null=True, blank=True)
    nickname_6 = models.CharField(max_length=255, verbose_name='Nickname 6', null=True, blank=True)
    nickname_7 = models.CharField(max_length=255, verbose_name='Nickname 7', null=True, blank=True)
    nickname_8 = models.CharField(max_length=255, verbose_name='Nickname 8', null=True, blank=True)
    nickname_9 = models.CharField(max_length=255, verbose_name='Nickname 9', null=True, blank=True)
    nickname_10 = models.CharField(max_length=255, verbose_name='Nickname 10', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Departament'
        verbose_name_plural = '1.Цех'



class Section(models.Model):
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    nickname_1 = models.CharField(max_length=255, verbose_name='Nickname 1', null=True, blank=True)
    nickname_2 = models.CharField(max_length=255, verbose_name='Nickname 2', null=True, blank=True)

    def __str__(self):
        return f"{self.departament.name}, {self.name}"
    
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = '2.Отдел'


class Phone(models.Model):
    FIO = models.CharField(max_length=255, verbose_name='Имя и Фамилия')
    job_title = models.CharField(max_length=255, verbose_name='Должность')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Отдел')
    number_1 = models.CharField(max_length=255, verbose_name='Внутренний номер')
    number_21 = models.CharField(max_length=255, verbose_name='Городской номер 1', null=True, blank=True)
    number_22 = models.CharField(max_length=255, verbose_name='Городской номер 2', null=True, blank=True)
    number_23 = models.CharField(max_length=255, verbose_name='Городской номер 3', null=True, blank=True)
    is_active_gorod_number = models.BooleanField(default=True, verbose_name='Показать городской номер')
    number_31 = models.CharField(max_length=255, verbose_name='Сотовый номер 1', null=True, blank=True)
    number_32 = models.CharField(max_length=255, verbose_name='Сотовый номер 2', null=True, blank=True)
    number_33 = models.CharField(max_length=255, verbose_name='Сотовый номер 3', null=True, blank=True)

 
    def __str__(self):
        return f"{self.FIO}-{self.job_title}"


    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = '3.Телефон номер'