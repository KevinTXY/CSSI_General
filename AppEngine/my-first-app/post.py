from google.appengine.ext import ndb

class Post(ndb.Model):
    image = ndb.BlobProperty()
    description = ndb.StringProperty()
