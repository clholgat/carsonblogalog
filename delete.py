import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import render
import logging
from BData import Post

class DeletePage(webapp.RequestHandler):
    def get(self, post):
        logging.info('in deletepage')
        render.header(self)
        render.body(self, 'showDelete.html', {'post': post})
        render.footer(self)
    
class DeleteYes(webapp.RequestHandler):
    def post(self):
        deleting = Post().get_by_id(int(self.request.get('post')))
        deleting.delete()
        self.redirect('/')

application = webapp.WSGIApplication([('/delete/(.*)', DeletePage),
                                      ('/deleteYes', DeleteYes)],
                                      debug=True)
                                      
def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
