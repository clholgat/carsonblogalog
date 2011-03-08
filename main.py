import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

#my bits and peices
import render
from BData import Post

class MainPage(webapp.RequestHandler):
    def get(self):
        query = Post.all().order('-date_posted')
        posts = query.fetch(limit=10, offset=0)

        render.header(self)
        render.body(self, 'showPosts.html', { 'posts' : posts})
        render.footer(self)

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
