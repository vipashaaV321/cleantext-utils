#author:Vipashaa
from django.http import HttpResponse
from django.shortcuts import render

#send response to server
# def about(request):
#     return HttpResponse("about vips")

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','vipasha')
    fullcaps = request.GET.get('fullcaps', 'off')
    removepunc=request.GET.get('removepunc','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    print(removepunc)

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"`\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        # analyze the text
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': "convert to uppercase", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': "remove new line", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': "remove extra space", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("you didnot select it")


# def removepunc(request):
#     print(request.GET.get('text','vipasha'))
#     #analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("Capitalize")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
# def charcount(request):
#     return HttpResponse("Char count")