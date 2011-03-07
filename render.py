import os

from google.appengine.ext.webapp import template
from google.appengine.api import users

nav = {
    'new' : '/',
    'top' : '/top',
    'browse' : '/browse',
    'submit' : '/submitquote',
    'login' : None,
    'login_text' : None
    }
    
def login(self):
    if users.get_current_user():
        nav['login'] = users.create_logout_url(self.request.uri)
        nav['login_text'] = 'Logout'
    else:
        nav['login'] = users.create_login_url(self.request.uri)
        nav['login_text'] = 'Login'
    
def header(self):
    login(self)    
    
    path = os.path.join(os.path.dirname(__file__), 'header.html')
    self.response.out.write(template.render(path, nav))
   
def footer(self):
    login(self)
    
    path = os.path.join(os.path.dirname(__file__), 'footer.html')
    self.response.out.write(template.render(path,nav))
    
def body(self, theFile, values):
    path = os.path.join(os.path.dirname(__file__), theFile)
    self.response.out.write(template.render(path, values))
