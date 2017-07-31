#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
from google.appengine.ext import ndb
#Kind (string)
#rating (int)
#Quantity (int)
#calories (int)
#Expiration (date)

class Company(ndb.Model):
    name = ndb.StringProperty()
    headquarters = ndb.StringProperty()
class Snack(ndb.Model):
    kind = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    url = ndb.StringProperty()
    company = ndb.KeyProperty(Company)
