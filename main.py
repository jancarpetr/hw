#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
import paths
from db import engine, Base

Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(paths.router)

@app.get("/")
def root():
	return {"message": "running"}
