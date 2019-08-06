from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField, SelectMultiple


from dependentmodels.models import Person, Car, AssignCar


class PersonForm(ModelForm):
    # add a field to select a car
    car = ModelMultipleChoiceField(queryset=Car.objects.all(), widget=SelectMultiple, label="Select Car")
    person = ModelChoiceField(queryset=Person.objects.all(), empty_label="Select User")

    class Meta:
        model = AssignCar
        fields = ('person', 'car')
        exclude = ['car',]