class DenyRule:

    __error = None
    __info = {}

    def __init__(self, error):
	self.__error = error
        pass

    def parseforbiddenAccess(self):
	
	self.__info["errorTag"] = "deny rule"
	self.__info["info"] = {}
        self.__info["info"]["Date"] = self.extractDateFromLine(self.__error)
	self.__info["info"]["ip"]   = self.extractIpFromLine(self.__error)
	self.__info["info"]["path"] = self.extractPathFromLine(self.__error)
	
	return self.__info
	
    def extractDateFromLine(self, line):
	line = line[1:]						# remove '['
	line = line[:line.find("]")]		# from start to index of ']'
	return line	
    
    def extractIpFromLine(self, line):
	index = line.find('client ')		#start index of "clint "
	index = index + len('client ')		#start index of socket
	line = line[index:]					#the line starts from the socket
	return line[:line.find(":")]		#the socket

    def extractPathFromLine(self,line):
	index = line.find('/')
	return line[index:]



def isError(errorLine):

    forbiddenAccessError ="client denied by server configuration"
    if forbiddenAccessError in errorLine:
	return True
    else:
  	return False
