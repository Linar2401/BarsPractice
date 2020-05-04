from django.db import models

# Create your models here.
from Barsik import settings
from account.models import *
import datetime


class Team(models.Model):
    # Тут я не знаю что писать, так что пока будет так.
    name = models.CharField(max_length=50, default='Team')
    managers = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managers', null=True)
    workers = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workers', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)


class Board(models.Model):
    teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, default='Board')


class Task(models.Model):
    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_P'
    FINISHED = 'FIN'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In progress'),
        (FINISHED, 'Finished'),
    )
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=4096)
    executor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='Executor', null=True,
                                    blank=True)
    role = models.CharField(max_length=4, choices=CustomUser.POSITION_CHOICES)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    deadline = models.DateTimeField(default=datetime.datetime.now())
