# mentor/views.py
from django.shortcuts import render, get_object_or_404
from accounts.models import CustomUser   # adjust if CustomUser is in another app
from django.shortcuts import redirect

def mentor_list(request):
    mentors = CustomUser.objects.filter(role='mentor', is_approved=True)
    return render(request, 'mentor_browse.html', {'mentors': mentors})

def mentor_detail(request, id):
    mentor = get_object_or_404(CustomUser, id=id, role='mentor')
    return render(request, 'mentor_detail.html', {'mentor': mentor})
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def book_appointment(request, id):
    mentor = get_object_or_404(CustomUser, id=id, role='mentor')

    if request.method == "POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')

        Appointment.objects.create(
            user=request.user,
            mentor=mentor,
            date=date,
            time=time,
            note=note
        )
        return redirect('mentor_detail', id=mentor.id)

    return render(request, 'book_appointments.html', {'mentor': mentor})
