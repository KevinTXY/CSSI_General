from google.appengine.ext import ndb
from post import Post

class User(ndb.Model):
    username = ndb.StringProperty()
    bio = ndb.StringProperty()
    posts = ndb.KeyProperty(Post, repeated = True)
    following = ndb.KeyProperty('User', repeated = True) #repeated allows many other users to be followed
