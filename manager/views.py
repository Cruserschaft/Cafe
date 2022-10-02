from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserReservations


def is_manager(user):
    return user.groups.filter(name="manager").exists()


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def reservation_list(request):
    lst = UserReservations.objects.filter(is_processed=False)
    return render(request, "reservation_list.html", context={"lst":lst})

@login_required(login_url="/login/")
@user_passes_test(is_manager)
def reservation_update(request, pk):
    UserReservations.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:reservation_list")
