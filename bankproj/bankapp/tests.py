# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase
from rest_framework.test import RequestsClient
import json
import sys
import requests
from dateutil.parser import parse


class BankTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        self.test_2 = []
        self.host = 'http://127.0.0.1:8080'
        with open('testfiles/http01.json') as f:
            for line in f:
                self.test_1.append(line)
        with open('testfiles/http02.json') as f:
            for line in f:
                self.test_2.append(line)

    def test_set_1(self):
        client = RequestsClient()
        for ro in self.test_1:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                url = self.host + row['request']['url'] + '/'
                res = requests.get(url)
            elif row['request']['method'] == "POST":
                res = requests.post(
                    self.host + row['request']['url'] + '/', json=row['request']['body'])
            
            self.assertEqual(res.status_code, row['response']['status_code'])
            self.assertEqual(json.loads(res.text), row['response']['body'])

    # def test_set_1(self):
    #     client = RequestsClient()
    #     for ro in self.test_1:
    #         row = json.loads(ro)
    #         res = {}
    #         if row['request']['method'] == "GET":
    #             url = self.host + row['request']['url'] + '/'
    #             res = requests.get(url)
    #         elif row['request']['method'] == "POST":
    #             res = requests.post(
    #                 self.host + row['request']['url'] + '/', json=row['request']['body'])
            
    #         self.assertEqual(res.status_code, row['response']['status_code'])
    #         self.assertEqual(json.loads(res.text), row['response']['body'])
            # if row['response']['headers'] != {}:
            #     self.assertEqual(
            #         res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            

    

   