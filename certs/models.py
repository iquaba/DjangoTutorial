from django.db import models


class Cert(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField()
    certs = models.ManyToManyField(Cert, blank=True, verbose_name='Certifications')

    def __unicode__(self):
        return self.name
