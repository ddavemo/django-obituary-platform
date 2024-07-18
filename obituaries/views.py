from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Obituary
from .forms import ObituaryForm

def obituary_form(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'obituary_form.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all().order_by('-submission_date')
    paginator = Paginator(obituaries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_obituaries.html', {'page_obj': page_obj})
