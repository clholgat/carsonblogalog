import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

#my bits and peices
import render

class MainPage(webapp.RequestHandler):
    def get(self):
        render.header(self)
        self.response.out.write('Something will go here soon')
        render.footer(self)

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
