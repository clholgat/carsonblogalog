import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users

from datetime import datetime

#my stuff
import render
from BData import Post

class PostPage(webapp.RequestHandler):
    def get(self):
        render.header(self)
        render.body(self, 'postPost.html', {'redirect' : '/postpost'})
        render.footer(self)
        
class PostPost(webapp.RequestHandler):
    def post(self):
        newPost = Post()
        newPost.title = self.request.get('title')
        newPost.body = self.request.get('body')
        newPost.date_posted = datetime.now()
        newPost.put()
        self.redirect('/')
        
application = webapp.WSGIApplication([('/post', PostPage),
                                      ('/postpost', PostPost)], 
                                      debug=True)
                                      
def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
