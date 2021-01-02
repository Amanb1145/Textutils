from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dicti = {'name' : 'Aman', 'place' : 'Haryana'}
    return render(request, 'index.html', dicti)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on" and len(djtext)>0:
        analyzed = djtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'FULL CAPS', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcounter == 'on'):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Count The Charecters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please Select an option <br> <a href='/'>back</a>")