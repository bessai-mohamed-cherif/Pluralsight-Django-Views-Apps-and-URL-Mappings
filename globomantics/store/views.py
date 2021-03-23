from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("Hello there, e-commerce store front coing through...")

def detail(request):
    return HttpResponse("detail")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple IPhone", "Lenovo", "Samsung", "Google")
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, "store/list.html", {'items': items})
    elif request.method == 'POST':
        return HttpResponseNotFound("POST Method is not allowed")