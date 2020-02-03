from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookmarks import apps
from bookmarks.forms import UserForm, ProfileForm
from bookmarky.settings import TIME_ZONE
from django.contrib.auth.models import User
from bookmarks.models import Bookmark, Tag, Profile


def index(request):
    """ index(request) -> HttpResponse: This function handles /bookmarks/ """
    str_response = f"Hello, world. You're at the {apps.BookmarksConfig.name} index.<br/>" \
                   f"Timezone is {TIME_ZONE}."
    return HttpResponse(str_response)


@login_required
@transaction.atomic
def update_profile(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            #messages.error(request, _('Please correct the error below.'))
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

