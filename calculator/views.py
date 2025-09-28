from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import InputForm
import math

def calculate(request):
    result = None
    error = None

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                error = "Value A is too small."
            elif b == 0:
                error = "Value B is zero and will not affect the result."
            elif c < 0:
                error = "Value C cannot be negative."
            else:
                cube = c ** 3
                if cube > 1000:
                    result = math.sqrt(cube) * 10
                else:
                    result = math.sqrt(cube) / a
                result += b
        else:
            error = "Invalid input."
    else:
        form = InputForm()

    return render(request, "calculator/result.html", {"form": form, "result": result, "error": error})

