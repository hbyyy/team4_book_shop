from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import BookRequest
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
        image_path ='/'+ book_info['image_path'].split('.')[1] + '.' + book_info['image_path'].split('.')[2]
        image_path_vol1 = image_path.replace(' ',"_")
        context = {
            'book_info' : book_info,
            'image_path' : image_path,
        }
        BookRequest.objects.create(
            title=book_info['title'],
            category=book_info['category'],
            book_intro=book_info['book_intro'],
            image=book_info['image_path'],

        )
        return render(request, 'request_success.html', context)


def book_request_confirm(request):
    bookrequests = BookRequest.objects.all()
    context = {
        'bookrequests': bookrequests
    }
    return render(request, 'books/request_list.html', context)