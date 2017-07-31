#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from snack import Snack
import jinja2
import os
from random import randint
import webapp2
from user import User
#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
###############
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
###############

class MainHandler(webapp2.RequestHandler):
    greetings = ["Hello World", "Hola Mundo","Bonjour le monde", "Ciao mondo", "Salut Lume", "Hei Verden", "Ahoj světe", "Hallo Welt", "Hallo Wereld"]
    def pageContent(self):
        amountGreetings = randint(0, len(self.greetings))
        pageResponse = ("<h1> This is my response </h1>")
        for index in range(amountGreetings):
            pageResponse += ("</br> %s. %s") % ((str(index + 1)), self.greetings[randint(0,amountGreetings-1)])
        return pageResponse

    def get(self):
        response = self.pageContent()
        self.response.write(response)

class MilkHandler(webapp2.RequestHandler):
    def get(self):
        produce = self.request.get("produce") # Grabbing produce info from URL
        pronum = self.request.get("pronum") #Grabbing number from URL
        self.response.write("Go get some milk and " + pronum + " " + produce ) # Writing to page
        if (int(pronum) >= 5):
            self.response.write("</br> Are you building a shrine for " + produce + " or what?")
        self.response.write("<h4> Milk </h4>")
        for index in range(int(pronum)):
            self.response.write("</br>" + "<h4>" +  produce + "</h4>")

class ImageHandler(webapp2.RequestHandler):

    def get(self):
        my_template = jinja_environment.get_template("templates/hello-world.html")
        name = self.request.get("myname")
        if (len(name) < 1):
            name = 'user'
        greetings = ['Hello','Bonjour', 'Hola', "What's up"]
        chosen_greeting = greetings[randint(0,(len(greetings)-1))]
        my_favorite_color = self.request.get("favorite_color")
        my_favorite_vegetable = self.request.get('favorite_veg')
        numchants = self.request.get("chants")
        if numchants == '':
            numchants = 0
        render_data = {
        'greeting' : chosen_greeting ,
        'name' : name ,
        'favorite_color' : my_favorite_color,
        'favorite_vegetable' : my_favorite_vegetable,
        'chants' : int(numchants),
        }  #sets data for placeholders
        self.response.write(my_template.render(render_data))
class SnackHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
        <html>
            <head>
            </head>
            <body>
                <form action='/snack'>
                    Kind: <input name = 'kind' type = 'text'/>
                    Rating: <input name = 'rating' type = 'text'/>
                    Quantity: <input name = 'quant' type = 'text'/>
                    Calories: <input name = 'cal' type = 'text' />
                    Image Url: <input name = 'iurl' type ='text' />
                    <input type = 'submit' />

                </form>
            </body>
        </html>
        """)
        snackKind = self.request.get("kind")
        snackRating = self.request.get("rating")
        snackQuantity = self.request.get("quant")
        snackCalories = self.request.get("cal")
        imageUrl = self.request.get('iurl')
        self.response.write("</br> <img src ='%s'/>" % (imageUrl))
        if snackRating == '':
            snackRating = 0
        if snackQuantity == '':
            snackQuantity = 0
        if snackCalories == '':
            snackCalories = 0
        mysnack = Snack(kind = snackKind, rating = int(snackRating), quantity = int(snackQuantity), calories = int(snackCalories), url = imageUrl)
        mysnack.put()
        self.response.write("</br> Currently Stored Snacks: ")
        query = Snack.query()
        results = query.fetch()
        usedList = []
        for i in range(len(results)):
            kind = results[i].kind
            if kind not in usedList:
                self.response.write("</br> %s" % (kind))
            usedList.append(kind)

class InstaHandler(webapp2.RequestHandler):
        def get(self):
            my_template = jinja_environment.get_template("templates/instagram.html")
            query = User.query()
            results = query.fetch
            render_data = {

            }
            usrname = self.request.get("usr")
            description = self.request.get("desc")
            poster = User(username = usrname,)
            poster.put()
            self.response.write(my_template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/image', ImageHandler),
    ('/snack', SnackHandler),
    ('/instagram', InstaHandler),
], debug=True)
