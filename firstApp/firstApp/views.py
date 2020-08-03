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
    cc=request.GET.get('cc','off')
    wc=request.GET.get('wc','off')
    lc = request.GET.get('lc', 'off')
    print(removepunc)

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"`\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
        # analyze the text
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': "convert to uppercase", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': "remove new line", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': "remove extra space", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(cc=="on"):
        data = djtext.replace(" ", "")
        # get the length of the data
        number_of_characters = len(data)
        print(number_of_characters)
        params = {'purpose': "Total character Count in text", 'analyzed_text':number_of_characters}
        # return HttpResponse(number_of_characters)
    if(wc=="on"):
        res = len(djtext.split())
        wcc=str(res)
        djtext = wcc
        params = {'purpose': "Total word Count in text", 'analyzed_text':djtext}
    if(lc=="on"):
        counter=0
        CoList = djtext.split("\n")

        for i in CoList:
            if i:
                counter += 1
        params = {'purpose': "Total Line Count in text", 'analyzed_text': counter}

    # else:
    #     return HttpResponse("you didnot select it")
    return render(request, 'analyze.html', params)

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