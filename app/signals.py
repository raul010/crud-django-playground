from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from app.models import Reporter


# @receiver(pre_save, sender=Reporter)
# def my_handler(sender, instance, **kwargs):
#     print('passou')
#
#     print(getattr(instance, '_conn', None))
#     print(sender)
#
#     for k in kwargs:
#         print(k)

# Envia Sinal
# conn = Signal(providing_args=["conn_"])
# conn.send(sender=None, conn_=connection.queries)
