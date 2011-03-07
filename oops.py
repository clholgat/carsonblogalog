import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import render

class OopsPage(webapp.RequestHandler):
    def get(self):
        render.header(self)
        self.response.out.write('You shouldn\'t be here, there\'s nothing here')
        render.footer(self)
        
application = webapp.WSGIApplication([('/.*', OopsPage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
