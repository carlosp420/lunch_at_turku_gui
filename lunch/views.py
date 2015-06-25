import datetime
import json
import requests

from django.shortcuts import render
from django.conf import settings


def index(request):
    APIKEY = settings.SCRAPINGHUB_KEY
    project_id = "17276"
    url = "https://storage.scrapinghub.com/items/{}".format(project_id)

    today = datetime.datetime.today()
    today_long_date = datetime.datetime.strftime(today, '%A, %d %b %Y')

    res = requests.get(url, auth=(APIKEY, ''))
    data = []
    for i in res.text.splitlines():
        i = json.loads(i)
        if i['day'] == today_long_date and i not in data:
            data.append(i)

    return render(request, 'lunch/base.html',
                  {'data': data, 'today': today_long_date})
