from django.shortcuts import render

def index(request):
    context = {
        'range_1_to_19': range(1, 20)  # 1 to 19 inclusive
    }
    return render(request, 'index.html', context)
