from django.db import models


class Schedule(models.Model):
    conference = models.CharField(max_length=30)

    def __str__(self):
        return self.conference


class Track(models.Model):
    name = models.CharField(max_length=30)
    schedule = models.ForeignKey(Schedule, related_name='tracks')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()

    def __str__(self):
        return "{0} ({1} mins.)".format(self.name, self.duration)


class Slot(models.Model):
    track = models.ForeignKey(Track, related_name='slots')
    type = models.ForeignKey(Type, related_name='slots')
    start_time = models.TimeField()
    name = models.CharField(max_length=300)
    by = models.CharField(max_length=100)

    def __str__(self):
        return "{0} ({1})".format(self.start_time, self.type)

    class Meta:
        ordering = ['start_time', 'name']
