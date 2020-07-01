from django.shortcuts import render

# Create your views here.

def indexView(request):
    ctx={'text': 'hello word', 'number':100}
    return render(request, 'basic_app/index.html', context=ctx)

def otherView(request):
    return render(request, 'basic_app/other.html')

def relativeView(request):
    return render(request, 'basic_app/relative_url_template.html')