import pyinotify
from NgParser import *
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
        print modify.parseforbiddenAccess()

    def process_IN_OPEN(self, event):
        print "OPEN event:", event.pathname

def main():
    wm = pyinotify.WatchManager()
    wm.add_watch("/home/sammman/logs/error.log", pyinotify.ALL_EVENTS, rec=True)

    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()
