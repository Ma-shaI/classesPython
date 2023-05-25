from .models import Projects, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Profile

def search_projects(request):
    all_data = Projects.objects.all()
    if request.GET.getlist('filter'):
        filters = request.GET.getlist('filter')
        tags = Tag.objects.filter(name__in=filters)
        filtered_data = Projects.objects.distinct().filter(Q(tags__in=tags))
        filter_name = 'filter'

        return filtered_data, filters, filter_name
    elif request.GET.getlist('filter_user'):
        filters = request.GET.getlist('filter_user')
        users = Profile.objects.filter(username__in=filters)

        projects = Projects.objects.distinct().filter(Q(owner__in=users))

        filter_name = 'filter_user'
        return projects, filters, filter_name
    elif request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        tags = Tag.objects.filter(name__icontains=search_query)
        projects = Projects.objects.distinct().filter(Q(title__iregex=search_query) |
                                                      Q(description__iregex=search_query) |
                                                      Q(owner__name__iregex=search_query) |
                                                      # Q(tags__name__icontains=search_query)
                                                      Q(tags__in=tags)
                                                      # Q(title__iregex=search_query)
                                                      )

        search_query = [request.GET.get('search_query')]
        filter_name = 'search_query'
        return projects, search_query, filter_name
    else:
        return all_data, '', ''


def paginate_projects(request, projects, results):
    page = request.GET.get('page', 1)
    # results = 3
    paginator = Paginator(projects, results)

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
