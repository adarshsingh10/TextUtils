# I have created this file -  Adarsh
from django.http import HttpResponse
from django.shortcuts import render

# Code for video 6

# def index(request):
#     return HttpResponse("hello Adarsh")

# def sidemen(request): 
#     return HttpResponse('''<a href="https://www.youtube.com/@Sidemen/videos">Sidemen Videos</a>''')

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse("remove punc")

def contactus(request):
    return render(request, 'contactus.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')              #Get the text from request
    #Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')              
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Extra Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charactercounter == 'on':
        count = 0
        for i in djtext:
            if i != ' ':
                count += 1
        analyzed = f'The number of characters is {count}'
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

def capfirst(request):
    return HttpResponse("capfirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")