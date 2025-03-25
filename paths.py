#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, db, gecko
from pydantic import BaseModel

router = APIRouter()

def get_db():
	dbs = db.SessionLocal()
	try:
		yield dbs
	finally:
		dbs.close()

@router.get("/krypto/")
def list_krypto(db : Session = Depends(get_db)):
	return crud.get_krypto(db)

class Item(BaseModel):
	symbol: str
	price: float

@router.post("/krypto/")
def add_krypto(item : Item, db : Session = Depends(get_db)):
	if gecko.symbol_exist(item.symbol):
		price = gecko.symbol_price(item.symbol)
		if price:
			return crud.create_krypto(db, item.symbol, item.price)
	return {"error": "not saved"}
