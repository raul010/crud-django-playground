from django.db import models

## 1 - ForeignKey (ManyToOne) ##

class Reporter(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        email = models.EmailField()

        def __str__(self):
            return u"%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter) #ManyToOne

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)