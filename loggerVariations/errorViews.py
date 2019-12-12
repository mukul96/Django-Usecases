from django.http import JsonResponse
import logging
from django.template import RequestContext



logger = logging.getLogger(__name__)


def error_400(request,Exception):
    logger.info("400 error has occurred")
    data="400 error has occured bad request"
    status=400
    finalDict={
        "data":data,
        "status":status
    }
    return JsonResponse(finalDict)






def error_403(request,Exception):
    logger.info("403 error has occurred")
    data="403 error has occured: resource is forbidden"
    status=403
    finalDict={
        "data":data,
        "status":status
    }
    return JsonResponse(finalDict)




def error_404(request,Exception=None):
    # logger.info("404 error has occurred")
    # data="404 error has occured: page not found"
    # status=404
    # finalDict={
    #     "data":data,
    #     "status":status
    # }
    # response = render_to_response("404.html")
    # response.status_code = 404
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
    return response
    return render(request,'myapp/404.html', status = 404)
    return render(request, 'ops404.html', data)
    #return JsonResponse(finalDict,status=404)



def error_500(request):
    logger.info("500 error has occurred")
    data="500 error has occured: internal server error"
    status=500
    finalDict={
        "data":data,
        "status":status
    }
    return JsonResponse(finalDict)
