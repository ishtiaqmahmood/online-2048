#coding=utf-8
from django.shortcuts import render,HttpResponse
import random
import json
from . models import RawTrain, Train, Station
# Create your views here.

def trains_search(request):
    if request.method == "POST":
        checi = request.POST["checiIn"].encode("utf-8")
        # Station.objects.create(name = 'name')
        print (Station.objects.all().values('id', 'name' ))
        # Station.objects.filter(name = "name")[1].delete()
        # train_no = Train.objects.filter(rawtrain__name=checi)
        # print (train_no)

        # label = "+checi+"
        res_dict = {
                "status": True,
                "message":["Test success!"],
                "trains":checi,
                "data":{ 'type': 'line',
                          'data': {
                             "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "saturday", "sunday"],
                             "datasets": [
                                        {
                                            "label": "train"+checi+"New",
                                            "fill": False,
                                            "lineTension": 0.1,
                                            "backgroundColor": "rgba(75,192,192,0.4)",
                                            "borderColor": "rgba(75,192,192,1)",
                                            "borderCapStyle": 'butt',
                                            "borderDash": [],
                                            "borderDashOffset": 0.0,
                                            "borderJoinStyle": 'miter',
                                            "pointBorderColor": "rgba(75,192,192,1)",
                                            "pointBackgroundColor": "#fff",
                                            "pointBorderWidth": 1,
                                            "pointHoverRadius": 4,
                                            "pointHoverBackgroundColor": "rgba(75,192,192,1)",
                                            "pointHoverBorderColor": "rgba(220,220,220,1)",
                                            "pointHoverBorderWidth": 2,
                                            "pointRadius": 6,
                                            "pointHitRadius": 10,
                                            "data": [random.randint(0,22),
                                                      random.randint(0,22),
                                                      random.randint(-5,22),
                                                      random.randint(0,22),
                                                      random.randint(-5,22),
                                                      random.randint(0,22),
                                                      random.randint(0,22)],
                                            "spanGaps": False,
                                        }
                                    ]
                                }
                }
            }
        return HttpResponse(json.dumps(res_dict))
    return render(request, 'search.html')
