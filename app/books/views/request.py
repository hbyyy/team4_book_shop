from django.core.files import File
from django.shortcuts import render, redirect

from books.models import BookRequest, Book
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

        image_path = book_info['image_path']
        with open(image_path, 'rb') as f:
            image = File(f)
            bookrequest = BookRequest(
                title=book_info['title'],
                category=book_info['category'],
                book_intro=book_info['book_intro'],
            )
            bookrequest.image.save(book_info['title'] + '.jpg', image, save=False)
            bookrequest.save()

        context = {
            'bookrequest': bookrequest,
        }

        return render(request, 'request_success.html', context)


def book_request_confirm(request, bookrequest_pk=None):
    if bookrequest_pk is None:
        bookrequests = BookRequest.objects.all()
        context = {
            'bookrequests': bookrequests
        }
        return render(request, 'books/request_list.html', context)
    else:
        bookrequest = BookRequest.objects.get(pk=bookrequest_pk)
        Book.objects.create(
            title=bookrequest.title,
            category=bookrequest.category,
            book_intro=bookrequest.book_intro,
            image=bookrequest.image,
        )
        bookrequest.delete()
        return redirect('books:book-list')
