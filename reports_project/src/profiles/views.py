from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import ProfileForms

# Create your views here.
@login_required
def my_profile_view(request):
    # profile = Profile.objects.get(user=request.user)
    profile = Profile.objects.get(user=request.user)
    form = ProfileForms(request.POST or None, request.FILES or None, instance= profile)
    confirm = False
    if form.is_valid():
        form.save()
        confirm = True
    context = {
        'profile': profile,
        "confirm": confirm,
        'form': form,
    }
    return render(request, 'profiles/profile.html', context)
