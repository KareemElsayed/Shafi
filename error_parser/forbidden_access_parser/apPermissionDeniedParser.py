
def isApPermissionDenied(line):
	return containErrorLineV1(line) or containErrorLineV2(line)

def containErrorLineV1(line):

	b1 = line.find("Permission denied") > -1
	b2 = line.find("file permissions deny server access") > -1
	return (b1 and b2)

def containErrorLineV2(line):

	b1 = line.find("Permission denied") > -1
	b2 = line.find("because search permissions are missing on a component of the path") > -1
	return (b1 and b2)


def extractDateFromLine(line):
	line = line[1:]						# remove '['
	line = line[:line.find("]")]		# from start to index of ']'
	return line

def extractSocketFromLine(line):
	index = line.find('client ')		#start index of "clint "
	index = index + len('client ')		#start index of socket
	line = line[index:]					#the line starts from the socket
	return line[:line.find("]")]		#the socket

def extractPathFromLineV1(line):
	index = line.find('/')
	return line[index:-1]


def extractPathFromLineV2(line):
	index = line.find("filesystem path '")			#start index of the word "filesystem path '"
	index = index + len("filesystem path '")		#start index of path
	line = line[index:]								#the line starts from the path
	return line[:line.find("'")]

def getApPermissionDeniedInfo(line):
	d = {}	
	d["errorTag"] = "permission denied"
	d["info"] = {}
	d["info"]["date"] = extractDateFromLine(line)	
	d["info"]["socket"] = extractSocketFromLine(line)
	if containErrorLineV1(line):
		d["info"]["path"] = extractPathFromLineV1(line)
	else:
		d["info"]["path"] = extractPathFromLineV2(line)

	return d

'''
version 2
[Thu Feb 11 03:05:40.914278 2016] [core:error] [pid 4958] (13)Permission denied: [client 127.0.0.1:37301] AH00035: access to /index.py denied (filesystem path '/var/www/test/index.py')
because search permissions are missing on a component of the path

version 1 
[Thu Feb 11 17:17:31.331754 2016] [core:error] [pid 5240] (13)Permission denied: [client 127.0.0.1:47007] AH00132: file permissions deny server access: /var/www/test/id.html
'''



