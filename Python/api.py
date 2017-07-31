#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
import urllib2
import json
response = urllib2.urlopen("https://uinames.com/api/")
content = response.read()
content_dict = json.loads(content)
print content_dict["name"]




# from datastore import Comment
# from random import randint
# import urllib2
# import json
#
#
#
#
# for i in range(10):
#     response = urllib2.urlopen("https://uinames.com/api/")
#     content = response.read()
#     content_dict = json.loads(content)
#     name = content_dict["name"]
#     region = content_dict["region"]
#     message = "Hello from %s!" % (region)
#     newScore = randint(0, 30000)
#     newnumres = randint(0, 400)
#     post = Comment(content = message, poster = name, score = newScore, numresponses = newnumres)
#     post.put()


#
# query = Comment.query(Comment.score <= 5000)
# resultsList = query.fetch()
# for i in range (len(resultsList)):
#    score = str(resultsList[i].score)
#    responses = str(resultsList[i].numresponses)
#    print "post " + str(i) + ": "
#    print "name: " + resultsList[i].poster
#    print "content: " + resultsList[i].content
#    print "score: " + score
#    print "responses: " + str(resultsList[i].numresponses)
