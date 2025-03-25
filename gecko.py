#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

headers = {"accept": "application/json", "x-cg-pro-api-key": "CG-r3GdVZ9E6G7rxH1AwWG391cL"}

def symbol_exist(symbol: str):
	url = "https://api.coingecko.com/api/v3/coins/{}/"
	url = url.format(symbol)
	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		data = response.json()
		if data:
			if (data["id"] == symbol):
				return True
	return False


def symbol_price(symbol: str):
	url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"
	url = url.format(symbol)
	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		data = response.json()
		if data:
			return data[symbol]["usd"]
	return None