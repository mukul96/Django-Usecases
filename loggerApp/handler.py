from django.http import HttpResponse,JsonResponse



def error_handler(func):
    def innerfunc(*args,**kwargs):
        try:
            data=func(*args,**kwargs)
            #data={"check":"the function worked"}
        except Exception as e:
            return JsonResponse({"data": "error has occured"})
        #return HttpResponse(data)
        return JsonResponse(data)

    return innerfunc