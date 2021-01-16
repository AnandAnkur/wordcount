from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext =request.GET['fulltext']
    worldlist = fulltext.split()
    worddict ={}
    for word in worldlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] =1
    sortword = sorted(worddict.items(),key= lambda x:x[1], reverse=True)
    return render (request ,'count.html',{'fulltext':fulltext , 'count':len(worldlist) , 'sortword':sortword})
def about(request):
    return render(request,'about.html')