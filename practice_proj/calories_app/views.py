from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
def home(req):
    """ Renders (/sends) home page of the calories app """
    return HttpResponse('<h1>calories app home</h1>')


class MealsViewAggregate(View):
    """ View class to handle meal list related requests """
    def get(self, request):
        """ GET: retrieve list of meals from the database """
        return JsonResponse({"message":"get all meals called"})

    def post(self, request):
        """ POST: add meal(s) to the database """
        return JsonResponse({"message":"post new meal(s) called"})

class MealsViewPiecemeal(View):
    """ View class to handle requests related to infividual meals: """

    def put(self, request, id):
        """ PUT: update individual meal of given ID """
        return JsonResponse({"message":"put updated meal called"})

    def delete(self, request, id):
        """ DELETE: remove meal with given ID from database """
        return JsonResponse({"message":"delete specific meal called... none must know my shame"})

    def get(self, request, id):
        """ GET: retrieve specific meal with given ID """
        return JsonResponse({"message":"get specific meal called"})

class MealsViewDay(View):
    """ View class to handle date related meal requests  """

    def get(self, request):
        """ GET: retrieve sum of calories for given date """
        return JsonResponse({"message":"get sum of calories in day called"})

