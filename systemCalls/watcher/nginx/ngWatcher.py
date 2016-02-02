import pyinotify
from NgParser import *
from error.ngForbiddenAccess.ngDenyRule import *
from pprint import pprint

class MyEventHandler(pyinotify.ProcessEvent):

    def process_IN_ACCESS(self, event):
        print "ACCESS event:", event.pathname

    def process_IN_ATTRIB(self, event):
        print "ATTRIB event:", event.pathname

    def process_IN_CLOSE_NOWRITE(self, event):
        print "CLOSE_NOWRITE event:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print "CLOSE_WRITE event:", event.pathname

    def process_IN_CREATE(self, event):
        print "CREATE event:", event.pathname

    def process_IN_DELETE(self, event):
        print "DELETE event:", event.pathname

    def process_IN_MODIFY(self, event):
        print "MODIFY event:", event.pathname
        modify = NgParser(event.pathname)
        error = modify.parseforbiddenAccess()
        try:
            test = NgDenyRule(error['client'], "/etc/nginx/conf.d/max.conf")
            test.seachDenyRule()
        except KeyError:
            print "Key is not exits"


    def process_IN_OPEN(self, event):
        print "OPEN event:", event.pathname
