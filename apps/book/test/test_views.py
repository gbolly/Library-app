from django.test import TestCase
# from django.test import LiveServerTestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
# from django_dynamic_fixture import G
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
# from selenium import webdriver
# from django.http import HttpRequest
from apps.book.views import *
from apps.book.models import Book, BookLease

class BookListViewTests(TestCase):
    """docstring for BookListViewTests"""
    def test_books_in_the_context(self):

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])
        Book.objects.create(title='getting things done',
                            author='david allen', 
                            isbn_number='22434643436',
                            date_recieved='2015-04-16',
                            quantity='3',
                            source='dave',
                            category='professional development'
                            )
        response =client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)