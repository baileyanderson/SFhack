from django.http import HttpResponse
from django.template import loader


def index(request):
    listIn = ["Thing1", "Thing2", "Thing3"]
    template = loader.get_template('main/index.html')
    context = {
        'listIn': listIn,
    }
    return HttpResponse(template.render(context, request))