from google.appengine.ext import ndb
class Comment(ndb.Model):
    content = ndb.StringProperty()
    poster = ndb.StringProperty()
    score = ndb.IntegerProperty()
    numresponses = ndb.IntegerProperty()

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
