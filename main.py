from systemCalls.watcher.nginx.ngWatcher import *
import fileinput

def main():
    wm = pyinotify.WatchManager()
    wm.add_watch("/home/sammman/logs/error.log", pyinotify.ALL_EVENTS, rec=True)

    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()
