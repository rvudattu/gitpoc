from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
import cx_Oracle

# Create your views here.



@api_view(['POST'])
def count_cur_sim(request):
    try:
        '''
        conn = cx_Oracle.connect('Apps/apps@omsddb.cswg.com:1521/omsd_app', encoding="UTF-8")
        query = f"select count(*) from apps.OMS_ALC_CURR_SIM_RESULTS"
        df = pd.read_sql(query, conn)
        res = df.to_dict('records')
        conn.close()
        return JsonResponse({"status": "success", "data": res})
        '''
        return JsonResponse({"status": "success", "data": "Response from Sub branch"})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

@api_view(['GET'])
def getresponse(request):
    try:
        return JsonResponse({"msg": "success."})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

