#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Float
from db import Base

class Krypto(Base):
    __tablename__ = "krypto"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True, index = True)
    price = Column(Float)


