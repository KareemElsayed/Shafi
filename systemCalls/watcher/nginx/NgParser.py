class NgParser:
    __fileName = None
    __forbiddenAccessError ="access forbidden by rule"

    def __init__(self, fileName):
        self.__fileName =  fileName

    def parseforbiddenAccess(self):
        failObj = open(self.__fileName,"r")
        errorLines =failObj.readlines()
        if errorLines:
            if self.__forbiddenAccessError in errorLines[-1]:
                tokenErrorLine = errorLines[-1].split()
                print "--------- token ---------"
                for findToken in tokenErrorLine:
                    if "#" in findToken:
                        indexToken = tokenErrorLine.index(findToken)
                DateTimeError = tokenErrorLine[:indexToken]
                MetaDataError =  " ".join(tokenErrorLine[indexToken+1:])
                MetaDataError = MetaDataError.split(",")
                forbiddenAccessObj= {}
                forbiddenAccessObj["date"]      = DateTimeError[0]
                forbiddenAccessObj['time']      = DateTimeError[1]
                forbiddenAccessObj['type']      = DateTimeError[2]
                forbiddenAccessObj['error']     = MetaDataError[0]
                forbiddenAccessObj['client']    = MetaDataError[1].split()[1]
                forbiddenAccessObj['server']    = MetaDataError[2].split()[1]
                forbiddenAccessObj['request']   = MetaDataError[3].split()[1]
                forbiddenAccessObj['host']      = MetaDataError[4].split()[1]
                forbiddenAccessObj['errorCode'] = tokenErrorLine[indexToken]
                return forbiddenAccessObj
                print "--------- token ---------"
            else:
                return {}
