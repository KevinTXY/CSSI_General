#!/usr/bin/env python
#
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

# import webapp2
# import json
# import urllib2
#
# class MainHandler(webapp2.RequestHandler):
#     search_term = 'puppy'
#     def get(self):
#         query = self.request.get("q")
#         giphy_data_source = urllib2.urlopen(
#             "http://api.giphy.com/v1/gifs/search?q='%s'&api_key=dc6zaTOxFJmzC&limit=10" % (query))
#         giphy_json_content = giphy_data_source.read()
#         parsed_giphy_dictionary = json.loads(giphy_json_content)
#         gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
#         self.response.write("<html> <body> <img src = '%s' /> </body> </html>" % (gif_url))
#         self.response.write("</br> <form> Search query: <input name = 'q' type = 'text' /></form>")
#
# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)
import os
import jinja2
import webapp2
import urllib
import urllib2
import json

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('q')
        index = self.request.get('i')
        
        if index == '':
            index = 0
        if query == '':
            query = 'puppy'
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': query, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        template = jinja_environment.get_template("templates/giphy.html")
        giphy_response = urllib2.urlopen(  #Accesses API
            base_url + urllib.urlencode(url_params))
        giphy_json = giphy_response.read()  #Strings -> Json
        giphy_data = json.loads(giphy_json)   #Parses Json into python dictionary
        url = giphy_data['data'][int(index)]['images']['original']['url']
        render_data = {
        'image_url': url,

        }
        self.response.write(template.render(render_data))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
