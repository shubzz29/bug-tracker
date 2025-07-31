from django.shortcuts import render, redirect
from .models import BugReport
from django.shortcuts import get_object_or_404
from .forms import BugReportForm

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'tracker/bug_list.html', {'bugs': bugs})

def bug_detail(request, pk):
    bug = get_object_or_404(BugReport, pk=pk)
    return render(request, 'tracker/bug_detail.html', {'bug': bug})    

def bug_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugReportForm()
    return render(request, 'tracker/bug_create.html', {'form': form})    