from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserReservations


@login_required(login_url="/login/")
def reservation_list(request):
    lst = UserReservations.objects.filter(is_processed=False)
    return render(request, "reservation_list.html", context={"lst":lst})
