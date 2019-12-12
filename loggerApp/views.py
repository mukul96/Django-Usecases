from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from loggerApp.handler import error_handler

# Create your views here.
import logging
logger = logging.getLogger(__name__)

@error_handler
def index(request,stringParameter):
    #a=1/0
    logger.info("this is an info response")
    finalDict={"data":"the code is working" ,"stringParameter":stringParameter}
    #return JsonResponse(finalDict,status=200)
    return finalDict


@csrf_exempt
def indexPost(request):
    if request.method=='POST':
        print(request.POST)
        #data=request.POST['data']
        print(request.body)
        data=json.loads(request.body.decode("utf-8"))
        data=data['data']
        return JsonResponse({"data":data})
    else:
        return JsonResponse({"data":"in indexPost error"})



def error_404(request,Exception=None):
    logger.info("404 error has occurred")
    data="404 error has occured: page not found"
    status=404
    finalDict={
        "data":data,
        "status":status
    }
    return JsonResponse(finalDict,status=404)




