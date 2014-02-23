#-*- coding: utf-8 -*-
import logging

from datetime import date
from django.core.management.base import NoArgsCommand
from django.db import models


from django.core.mail import send_mail

class Command(NoArgsCommand):
    def handle_noargs(self, **options): pass
    pass

logging.basicConfig(level=logging.DEBUG)

def teste_2():
    from app.models import Publication, Article


    p1 = Publication(title='The Python Journal')
    p1.save()
    p2 = Publication(title='Science News')
    p2.save()
    p3 = Publication(title='Science Weekly')
    p3.save()

    a1 = Article(headline='Django lets you build Web apps easily')

    # a1.publications.add(p1) #You can’t associate it with a Publication until it’s been saved:
    a1.save()
    a1.publications.add(p1)

    a2 = Article(headline='NASA uses Python')
    a2.save()
    a2.publications.add(p1, p2)


    print()

    print()

    print()

    print()

    print()

    print()

    print()

# def teste_1():
#     # Create a few Reporters:
#
#     from app.models import Article, Reporter
#
#     r = Reporter(first_name='John', last_name='Smith', email='john@example.com')
#     #r._conn = 'named attribute'
#
#     r.save()
#
#     r2 = Reporter(first_name='Paul', last_name='Jones', email='jaul@example.com')
#     r2.save()
#
#
#     # Create an Article
#     a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
#     a.save()
#
#     print(a.reporter.id) # 1
#
#     print(a.reporter) # <Reporter: John Smith>
#
#     r = a.reporter
#
#     print(r.first_name, r.last_name) #('John', 'Smith')
#
#
#     # Create an Article via the Reporter object:
#     new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
#     print(new_article)
#
#     new_article2 = Article(headline="Paul's story", pub_date=date(2005, 4, 17))
#     print(r.article_set.add(new_article2)) # John Smith
#     print(new_article2.reporter.id) # 1
#     print(r.article_set.all()) # <Article: John's second story>, <Article: Paul's story>, <Article: This is a test>
#
#
#     # Add the same article to a different article set - check that it moves
#     r2.article_set.add(new_article2)
#     print(new_article2.reporter.id) # 2
#     print(new_article2.reporter) # <Reporter: Paul Jones>
#     print(r.article_set.all())
#
#     # r.article_set.add(r2) # wrong type raises TypeError:
#
#     print(r.article_set.count())
#
#     print(r.article_set.filter(headline__startswith='This')) #[<Article: This is a test>]
#
#     ## Find all Articles for any Reporter whose first name is "John".
#
#     # Realizam INNER JOIN entre Article e Reporter
#     print(Article.objects.filter(reporter__first_name__exact='John'))
#     print(Article.objects.filter(reporter__first_name__exact='John', reporter__last_name__exact='Smith'))
#
#     # Relacionamento natural, não realizou entradas na base
#     Article.objects.filter(reporter__pk=1)
#     Article.objects.filter(reporter=1)
#     Article.objects.filter(reporter=1)
#
#     # Relacionamento não natural (INNER JOIN), realiza consulta todas as vezes
#     print(Reporter.objects.filter(article__pk=1))
#     print(Reporter.objects.filter(article=1))
#     print(Reporter.objects.filter(article=a))
#
#     print(Article.objects.filter(reporter__in=[1,2]).distinct())
#
#     print(Article.objects.filter(reporter__in=[r,r2]).distinct())
#     # Realiza o SELECT (DISTINCT) * FROM article  WHERE article.reporter_id IN (SELECT reporter.id ...)
#     print(Article.objects.filter(reporter__in=Reporter.objects.filter(first_name='John')).distinct())
#
#     print(Reporter.objects.filter(article__headline__startswith='This'))
#
#     print(Reporter.objects.filter(article__headline__startswith='This').distinct())
#
#     print(Reporter.objects.filter(article__headline__startswith='This').count())
#
#     print(Reporter.objects.filter(article__reporter__first_name__startswith='John'))
#
# teste_1()

teste_2()


# print (Article.objects.filter(name="my name").query)


# Signals pode ser visto como um AOP, como AspectJ do Java.
# @receiver(post_save, sender=Reporter)
# def sql_log_handler(sender, instance, **kwargs):
#     """
#     Imprime Queries no console
#     """
#
      #Imports
#     from django.core.signals import request_finished
#     from django.db.models.signals import pre_save, post_save
#     from django.dispatch.dispatcher import receiver
#     from django.db import connection

#     # print(getattr(instance, '_conn', None))
#     # for query in connection.queries:
#     #     logging.info(query['sql'])
#     # print('\n')

