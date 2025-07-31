from django.shortcuts import render, get_object_or_404, redirect
from .models import BugReport
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

def edit_bug(request, pk):
    bug = get_object_or_404(BugReport, pk=pk)

    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = BugReportForm(instance=bug)

    return render(request, 'tracker/bug_edit.html', {'form': form, 'bug': bug})     