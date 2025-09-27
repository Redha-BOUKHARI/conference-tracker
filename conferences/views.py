from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Conference

def home(request):
    conferences = Conference.objects.filter(submission_deadline__gte=timezone.now()).order_by('submission_deadline')[:6]
    
    total = Conference.objects.count()
    urgent = Conference.objects.filter(
        submission_deadline__gte=timezone.now(),
        submission_deadline__lte=timezone.now() + timezone.timedelta(days=7)
    ).count()
    upcoming = Conference.objects.filter(
        submission_deadline__gte=timezone.now(),
        submission_deadline__lte=timezone.now() + timezone.timedelta(days=30)
    ).count()
    
    context = {
        'conferences': conferences,
        'total_conferences': total,
        'urgent_count': urgent,
        'upcoming_count': upcoming,
    }
    return render(request, 'conferences/home.html', context)

def conference_list(request):
    conferences = Conference.objects.all().order_by('submission_deadline')
    return render(request, 'conferences/conference_list.html', {'conferences': conferences})

def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conferences/conference_detail.html', {'conference': conference})
    