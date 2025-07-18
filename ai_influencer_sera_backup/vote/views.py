from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def vote(request):
    return render(request, 'vote.html')