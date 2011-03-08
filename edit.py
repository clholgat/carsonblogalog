import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#my stuff
import render
from BData import Post

class EditPage(webapp.RequestHandler):
    def get(self):
        posts = Post.all().order('-date_posted').fetch(20)
        
        render.header(self)
        render.body(self, 'showEditAll.html', {'posts' : posts})
        render.footer(self)
        
class EditOnePage(webapp.RequestHandler):
    def get(self, post):
        editing = Post.get_by_id(int(post))
        
        render.header(self)
        render.body(self, 'showEditOne.html', {'post' : editing, 
                                               'redirect' : '/update'})
        render.footer(self)
        
class UpdatePage(webapp.RequestHandler):
    def post(self):
      edited = Post.get_by_id(int(self.request.get('id')))
      edited.title = self.request.get('title')
      edited.body = self.request.get('body')
      edited.put()
      self.redirect('/view/%s' % edited.key().id())
      
        
application = webapp.WSGIApplication([('/edit', EditPage),
                                      ('/edit/(.*)', EditOnePage),
                                      ('/update', UpdatePage)],
                                      debug=True)
                                      
def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
