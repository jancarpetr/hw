#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import models
from sqlalchemy.orm import Session

def get_krypto(db : Session):
	return db.query(models.Krypto).all()

def create_krypto(db : Session, name : str, price : float):
	db_krypto = models.Krypto(name = name, price = price)
	db.add(db_krypto)
	db.commit()
	db.refresh(db_krypto)
	return db_krypto


