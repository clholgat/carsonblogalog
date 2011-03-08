
from google.appengine.ext import db

class Post(db.Model):
    date_posted = db.DateTimeProperty(auto_now_add=True)
    date_edited = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    body = db.TextProperty()
    
class Comment(db.Model):
    date = db.DateTimeProperty(auto_now_add=True)
    comment = db.StringProperty(multiline=True)
    user = db.UserProperty()
