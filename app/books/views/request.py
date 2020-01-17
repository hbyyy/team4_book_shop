from django.http import HttpResponse
from django.shortcuts import render

from .. import crawler
from ..crawler import research_page_crawler


def book_request_view(request):
    if request.method == 'POST':
        value = request.POST['q']
        book_list = research_page_crawler(value)
        print('----------------------------------------')
        print(book_list)
        print('----------------------------------------')
        context = {
            'book_list': book_list
        }
        return render(request, 'request.html', context)

    elif request.method == 'GET':
        value = request.GET.get('keyword', 'java')
        book_list = research_page_crawler(value)
        print('----------------------------------------')
        print(book_list)
        print('----------------------------------------')
        context = {
            'book_list': book_list
        }
        return render(request, 'request.html', context)



