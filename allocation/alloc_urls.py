import django.conf.urls
from django.urls import path, include
from django.urls import path

from allocation.views import count_cur_sim, getresponse, test_api_new

# urlpatterns =[
# django.conf.urls.url(r'^count_cur_sim', count_cur_sim, name="To get count of rows.") ,
# ]

urlpatterns =[
    path(r'count_cur_sim', count_cur_sim, name="To get count of rows."),
    path('getresponse', getresponse, name="To get response."),
    path('test_api_new', test_api_new, name="Test api in dev.")
]
