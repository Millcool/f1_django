from django.shortcuts import render
from .models import Result


def grand_prix_results(request):
    results = Result.objects.order_by('position')
    return render(request, 'grand_prix_results.html', {'results': results})
