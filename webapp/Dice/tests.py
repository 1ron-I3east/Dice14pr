from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from htmltext import find_text, format_html, gettext
from .models import*
import pandas as pd
import requests
import openpyxl

# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly_1(self):
        response = self.client.get('haha')
        self.assertEqual(response.status_code, 404)

    def test_index_loads_properly_2(self):
        url1 = reverse('main')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)

 # error content
    def test_index_loads_properly_3(self):
        url1 = reverse('main')
        response = self.client.get(url1)
        self.assertNotEqual(response.content, '<!DOCTYPE html>\n<html lang="en">\n<head>\n')

    def test_index_loads_properly_4(self):
        response = self.client.get('https:django/127')
        self.assertEqual(response.status_code, 404)
# error response
    def test_index_loads_properly_5(self):
        response = self.client.get('https:django/127')
        self.assertNotEqual(response, '<HttpResponseNotFound status_code=404, "text/html; charset=utf-8">')

class CharacterApiTest(APITestCase):
    def test_response_correct_1(self):
        url = reverse('testapi')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_response_correct_2(self):
        url2 = reverse('testapi')
        response = self.client.get(url2)
        self.assertEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2}, 'id': {0: 1, 1: 2, 2: 3}, 'name': {0: 'lev', 1: 'aidar', 2: 'Alex'}, 'Hero': {0: 'albus', 1: 'karl', 2: 'tree'}, 'Race': {0: 'ulf', 1: 'hnome', 2: 'treeman'}, 'Strength': {0: 6, 1: 7, 2: 0}, 'Constitution': {0: 
6, 1: 4, 2: 10}, 'Dexterity': {0: 3, 1: 7, 2: 0}, 'Intelligence': {0: 5, 1: 10, 2: 10}, 'Wisdom': {0: 5, 1: 5, 2: 10}, 'Charisma': {0: 10, 1: 10, 2: 10}, 'url': 'http://127.0.0.1:8000/download'})
# error id !=number
    def test_response_correct_3(self):
        url2 = reverse('testapi')
        response = self.client.get(url2)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2}, 'number': {0: 1, 1: 2, 2: 3}, 'name': {0: 'lev', 1: 'aidar', 2: 'Alex'}, 'Hero': {0: 'albus', 1: 'karl', 2: 'tree'}, 'Race': {0: 'ulf', 1: 'hnome', 2: 'treeman'}, 'Strength': {0: 6, 1: 7, 2: 0}, 'Constitution': {0: 
6, 1: 4, 2: 10}, 'Dexterity': {0: 3, 1: 7, 2: 0}, 'Intelligence': {0: 5, 1: 10, 2: 10}, 'Wisdom': {0: 5, 1: 5, 2: 10}, 'Charisma': {0: 10, 1: 10, 2: 10}, 'url': 'http://127.0.0.1:8000/download'})
 # error Wisdm
    def test_response_correct_4(self):
        url2 = reverse('testapi')
        response = self.client.get(url2)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2}, 'id': {0: 1, 1: 2, 2: 3}, 'name': {0: 'lev', 1: 'aidar', 2: 'Alex'}, 'Hero': {0: 'albus', 1: 'karl', 2: 'tree'}, 'Race': {0: 'ulf', 1: 'hnome', 2: 'treeman'}, 'Strength': {0: 6, 1: 7, 2: 0}, 'Constitution': {0: 
6, 1: 4, 2: 10}, 'Dexterity': {0: 3, 1: 7, 2: 0}, 'Intelligence': {0: 5, 1: 10, 2: 10}, 'Wisdm': {0: 5, 1: 5, 2: 10}, 'Charisma': {0: 10, 1: 10, 2: 10}, 'url': 'http://127.0.0.1:8000/download'})   


# error zero
    def test_response_correct_5(self):
        url2 = reverse('testapi')
        response = self.client.get(url2)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 0: 0, 0: 0}, 'id': {0: 1, 1: 2, 2: 3}, 'name': {0: 'lev', 1: 'aidar', 2: 'Alex'}, 'Hero': {0: 'albus', 1: 'karl', 2: 'tree'}, 'Race': {0: 'ulf', 1: 'hnome', 2: 'treeman'}, 'Strength': {0: 6, 1: 7, 2: 0}, 'Constitution': {0: 
6, 1: 4, 2: 10}, 'Dexterity': {0: 3, 1: 7, 2: 0}, 'Intelligence': {0: 5, 1: 10, 2: 10}, 'Wisdm': {0: 5, 1: 5, 2: 10}, 'Charisma': {0: 10, 1: 10, 2: 10}, 'url': 'http://127.0.0.1:8000/download'})   
          
 