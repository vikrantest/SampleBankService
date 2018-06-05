# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import sys
import os
import requests
from django.conf import settings
from django.test import TestCase
from rest_framework.test import RequestsClient
from dateutil.parser import parse
import subprocess


class BankTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        self.test_2 = []
        self.test_3 = []
        self.host = 'http://localhost:8000'
        # curr = os.getcwd()
        # os.chdir(curr+'/buildapp')
        # subprocess.call(['./data_build'])
        # os.chdir(curr)
        with open('testfiles/http01.json') as f:
            for line in f:
                self.test_1.append(line)
        with open('testfiles/http02.json') as f:
            for line in f:
                self.test_2.append(line)
        with open('testfiles/http03.json') as f:
            for line in f:
                self.test_3.append(line)

    def testSet1(self):
        client = RequestsClient()
        res = client.post('http://localhost:8000/bankapp/v1/account/',json={})
        for ro in self.test_1:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                url = self.host + row['request']['url'] + '/'
                print url
                res = client.get('http://localhost:8000' + row['request']['url'] + '/')
                print res.text
            elif row['request']['method'] == "POST":
                res = client.post(
                    self.host + row['request']['url'] + '/', json=row['request']['body'])
            
            self.assertEqual(res.status_code, row['response']['status_code'])
            self.assertEqual(json.loads(res.text), row['response']['body'])

    def testSet2(self):
        client = RequestsClient()
        res = client.post('http://localhost:8000/bankapp/v1/account/',json={})
        for ro in self.test_2:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                url = self.host + row['request']['url'] + '/'
                res = client.get(url)
            elif row['request']['method'] == "POST":
                res = client.post(
                    self.host + row['request']['url'] + '/', json=row['request']['body'])
            
            self.assertEqual(res.status_code, row['response']['status_code'])
            self.assertEqual(json.loads(res.text), row['response']['body'])

    def testSet3(self):
        client = RequestsClient()
        res = client.post('http://localhost:8000/bankapp/v1/account/',json={})
        for ro in self.test_3:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                url = self.host + row['request']['url'] + '/'
                res = client.get(url)
            elif row['request']['method'] == "POST":
                res = client.post(
                    self.host + row['request']['url'] + '/', json=row['request']['body'])
            
            self.assertEqual(res.status_code, row['response']['status_code'])
            self.assertEqual(json.loads(res.text), row['response']['body'])
            

    

   