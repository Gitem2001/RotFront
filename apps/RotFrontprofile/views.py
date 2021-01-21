from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RotFrontprofileForm
# Create your views here.
def  RotFrontprofile(request, username):
    user = get_object_or_404(User,username=username)

    context = {
        'user': user
    }

    return render(request, 'RotFrontprofile/RotFrontprofile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = RotFrontprofileForm(request.POST, request.FILES, instance=request.user.RotFrontprofile)

        if form.is_valid():
            form.save()

            return redirect('RotFrontprofile', username=request.user.username)
    else:
        form = RotFrontprofileForm(instance=request.user.RotFrontprofile)

    context = {
        'user':request.user,
        'form':form
    }

    return render(request, 'RotFrontprofile/edit_profile.html', context)

@login_required
def follow_roter(request, username):
    user = get_object_or_404(User,username=username)

    request.user.RotFrontprofile.follows.add(user.RotFrontprofile)

    return redirect('RotFrontprofile', username=username)

@login_required
def unfollow_roter(request, username):
    user = get_object_or_404(User,username=username)

    request.user.RotFrontprofile.follows.remove(user.RotFrontprofile)

    return redirect('RotFrontprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User,username=username)

    return render(request, 'RotFrontprofile/followers.html', {'user':user})

def follows(request, username):
    user = get_object_or_404(User,username=username)

    return render(request, 'RotFrontprofile/follows.html', {'user':user})    