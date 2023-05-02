from .models import Projects, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Projects.objects.distinct().filter(Q(title__iregex=search_query) |
                                                  Q(description__iregex=search_query) |
                                                  Q(owner__name__iregex=search_query) |
                                                  # Q(tags__name__icontains=search_query)
                                                  Q(tags__in=tags)
                                                  # Q(title__iregex=search_query)
                                                  )
    return projects, search_query


def paginate_projects(request, projects, results):
    page = request.GET.get('page', 1)
    # results = 3
    paginator = Paginator(projects, results, allow_empty_first_page=False)

    # try:
    #     pr = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     pr = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     pr = paginator.page(page)
    projects = paginator.get_page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return projects, custom_range