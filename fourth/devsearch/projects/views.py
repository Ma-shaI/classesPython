from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .utils import search_projects, paginate_projects
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from users.models import Profile


def projects(request):
    page_obj, filters, filter_name = search_projects(request)
    page_obj, custom_range = paginate_projects(request, page_obj, 3)

    context = {
        'projects': page_obj,
        # 'search_query': search_query,
        # 'paginator': paginator,
        'custom_range': custom_range,
        # 'page_obj': page_obj,
        'selected_filters': filters,
        'options': Tag.objects.all(),
        'filter_name': filter_name,
        'users': Profile.objects.all()
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Projects.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_obj
        review.owner = request.user.profilert
        review = form.save()

        project_obj.get_vote_count()
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=project_obj.id)
    return render(request, 'projects/single-project.html', {'project': project_obj, 'form': form})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectsForm()

    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
    if form.is_valid():
        project = form.save(commit=False)
        project.owner = profile
        form.save()
        return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    form = ProjectsForm(instance=project)
    if request.method == 'POST':
        new_tags = request.POST.get('new_tags').replace(',', ' ').split()

        form = ProjectsForm(request.POST, request.FILES, instance=project)
        if form.is_valid():

            for tag in new_tags:
                print(tag)
                tag1, created = Tag.objects.get_or_create(name=tag)
            project = form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    contex = {
        'object': project
    }
    return render(request, 'projects/delete.html', contex)
