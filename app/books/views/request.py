from django.http import HttpResponse
from django.shortcuts import render, redirect

from .. import crawler
from ..crawler import research_page_crawler, detail_page_crawler


def book_request_view(request):
    # if request.method == 'POST':
    #     value = request.POST['q']
    #     book_list = research_page_crawler(value)
    #     print('----------------------------------------')
    #     print(book_list)
    #     print('----------------------------------------')
    #     context = {
    #         'book_list': book_list
    #     }
    #     return render(request, 'request.html', context)

    try:
        value = request.GET['keyword']
        book_list = research_page_crawler(value)
        if book_list is None:
            return redirect('books:book-request')
        context = {
            'book_list': book_list
        }
        return render(request, 'request.html', context)
    except KeyError:
        return render(request, 'request.html')


def book_request_save_view(request):
    if request.method == 'POST':
        url = request.POST['url']
        book_info = detail_page_crawler(url)
        print(book_info)
        return HttpResponse(book_info)