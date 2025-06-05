from django.shortcuts import render, redirect
from .models import MCQ
from .forms import MCQForm

def mcq_list(request):
    mcqs = MCQ.objects.all()
    return render(request, 'app/mcq_list.html', {'mcqs': mcqs})

def add_mcq(request):
    if request.method == 'POST':
        form = MCQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mcq_list')
    else:
        form = MCQForm()
    return render(request, 'app/add_mcq.html', {'form': form})