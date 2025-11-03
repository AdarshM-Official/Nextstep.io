from django.shortcuts import render

# Create your views here.
def careers_view(request):
    return render(request, 'roadmap.html')


