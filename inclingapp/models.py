from django.db import models


class Tile(models.Model):
    PENDING = 'PEN'
    LIVE = 'LIV'
    ARCHIVED = 'ARC'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (LIVE, 'Live'),
        (ARCHIVED, 'Archived'),
    )
    launch_date = models.DateTimeField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    def __str__(self):
        return str(self.id)


class Task(models.Model):
    SURVEY = 'SUR'
    DISCUSSION = 'DIS'
    DIARY = 'DIA'
    TYPE_CHOICES = (
        (SURVEY, 'Survey'),
        (DISCUSSION, 'Discussion'),
        (DIARY, 'Diary'),
    )
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    description = models.CharField(max_length=500)
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=SURVEY,
    )
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
