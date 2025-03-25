#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
response = requests.post("http://127.0.0.1:8000/krypto/", json = {"symbol" : "ethereum", "price" : "11"})