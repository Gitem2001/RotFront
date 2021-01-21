from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import rot

@login_required
def feed(request):
    userids = [request.user.id]

    for roter in request.user.RotFrontprofile.follows.all():
        userids.append(roter.user.id)


    rots = rot.objects.filter(created_by_id__in=userids)

    return render(request,'feed/feed.html', {'rots':rots})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        roters = User.objects.filter(username__icontains=query)
    else:
        roters = []

    context = {
        'query':query,
        'roters':roters
    }

    return render(request, 'feed/search.html', context)