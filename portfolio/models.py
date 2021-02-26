from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    TYPES = (
        ('Webapp', 'Webapp'),
        ('DS', 'Data Science'),
        ('Courses', 'Courses'),
    )
    type = models.CharField(max_length=7, default='None', choices=TYPES)

    def __str__(self):
        return self.title
