from django.shortcuts import render, redirect
from .models import Projects, Tag
from .forms import ProjectsForm
from django.contrib.auth.decorators import login_required


def projects(request):
    pr = Projects.objects.all()
    context = {'projects': pr}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Projects.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})


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
        # new_tags = request.POST.get('tags').replace(',', ' ').split()

        form = ProjectsForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            # for tag in new_tags:
            #     tag1, created = Tag.objects.get_or_create(name=tag)
            #     project.tags.add(tag1.name)
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
