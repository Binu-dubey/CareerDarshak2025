from django.shortcuts import render, get_object_or_404
from .models import CareerOption,Branch
from collections import defaultdict
# Create your views here.
def library(request):
    career_options = CareerOption.objects.all()
    stream_groups = defaultdict(list)

    for career in career_options:
        stream_groups[career.stream_type].append(career)

    return render(request, 'careerlibrary/library.html', {
        'stream_groups': dict(stream_groups)
    })
 
def career_detail(request, career_id):
    career_option = get_object_or_404(CareerOption, pk=career_id)
    branches = career_option.branches.all() 
    return render(request, 'careerlibrary/career_detail.html',{
        'career_option': career_option,
        'branches' : branches
    })
def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    return render(request, 'careerlibrary/branch_detail.html',{
        'branch': branch
    })
def path(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    return render(request, 'careerlibrary/pathbook.html',{
        'branch': branch
    })
