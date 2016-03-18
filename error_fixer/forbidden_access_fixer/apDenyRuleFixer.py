class DenyRule():

    """Search for deny rules in nginx config file"""

    __ipAddress = None
    __pathConfigFile = None
    __denyRule = "deny from"
    __allowRule = "allow"

    def __init__(self):
        pass

    def seachDenyRule(self, errorInfo):
		
        configFileObj = open("/etc/apache2/000-default.conf", "r")
        for line in configFileObj.readlines():
            if self.__denyRule in line:
                line = line.strip()
                print line
            else:
                continue

        configFileObj.close()

    def fixByAllowRule(self):
        for line in fileinput.input(self.__pathConfigFile, inplace=True):
            print line.replace('deny ' + self.__ipAddress, 'allow ' + self.__ipAddress),
        test = subprocess.Popen(["service nginx restart"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()
        for i in test:
            print i

    def fixByRemove(self):
        for line in fileinput.input(self.__pathConfigFile, inplace=True):
            print line.replace('deny ' + self.__ipAddress+";", ''),
        test = subprocess.Popen(["service nginx restart"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()
        for i in test:
            print i

