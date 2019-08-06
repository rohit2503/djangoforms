from django.shortcuts import render, redirect

# Create your views here.
from dependentmodels.forms import PersonForm
from dependentmodels.models import Car, AssignCar, Person


def my_view(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        personal_form = PersonForm(request.POST)

        if personal_form.is_valid():
            cars = request.POST.getlist('car')
            person = request.POST.getlist('person')

            for car in cars:
                assigncar = AssignCar.objects.create(car=Car.objects.get(id=car),
                                                     person=Person.objects.get(id=person[0]))
                assigncar.save()

        redirect("/djangoform")

    else:
        personal_form = PersonForm()
        personal_form.fields['car'].choices = [(car.id, car.make) for car in Car.objects.all()]


    return render(request, "my_view.html", {'form': personal_form})