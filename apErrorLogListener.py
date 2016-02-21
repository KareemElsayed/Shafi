
import pyinotify

from error_fixer.errorFixer import *
from error_parser.errorInfo import *

def errorListener(path,eh):
	wm = pyinotify.WatchManager()
	wm.add_watch(path, pyinotify.IN_MODIFY, rec=True)
	notifier = pyinotify.Notifier(wm, eh)
	notifier.loop()


def readLastErrorLine(path):
	fileRows = []
	try:
		f1 = open(path)
		fileRows = f1.readlines()[-1:]		#read last line
		f1.close()
	except Exception:
		print("can not open target with the given path..")
	return fileRows


class MyEventHandler(pyinotify.ProcessEvent):
	
	def __init__(self,p1):
		self.errorLogPath = p1
		errorListener(p1,self)

	def process_IN_MODIFY(self, event):
		errorLines = readLastErrorLine(self.errorLogPath)
		if errorLines:
			ed = getErrorInfo(errorLines[0])			# from errorInfo module
			fixError(ed)
			
		

















