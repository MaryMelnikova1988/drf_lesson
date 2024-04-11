from celery import shared_task, Celery

from vehicle.models import Car, Moto

# app = Celery('tasks', backend='redis://127.0.0.1:6379', broker='redis://127.0.0.1:6379')
# app.conf.broker_url = 'redis://127.0.0.1:6379/0'


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print("Неверный пробег")
                    break
def check_filter():
    filter_price = {"price__lte": 500}

    if Car.objects.filter(**filter_price).exists():
        print("Отчет по фильтру")
        # send_mail(subject="отчет по фильтру",
        #           message='у на машины под ваш фильтр, заходите на сайт',
        #           from_email='admin@sky.pro',
        #           recipient_list=[user.email])