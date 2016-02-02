import fileinput
import subprocess

class NgDenyRule():

    """Search for deny rules in nginx config file"""

    __ipAddress = None
    __pathConfigFile = None
    __denyRule = "deny"
    __allowRule = "allow"

    def __init__(self, ipRejected, path):
        self.__ipAddress = ipRejected
        self.__pathConfigFile = path

    def seachDenyRule(self):
        configFileObj = open(self.__pathConfigFile, "r")

        for line in configFileObj.readlines():
            if self.__denyRule in line:
                line = line.strip()
                print line

                if self.__ipAddress in line:
                    print "[1] Fix by Allow Rule"
                    print "[2] Fix by Remove Deny Rule"
                    print "[0] Abort Operation"
                    fixCode = raw_input("Please Enter choose : ")
                    if fixCode == "1":
                        print "fix by allow rule"
                        self.fixByAllowRule()
                    elif fixCode == "2":
                        print "fix by remove rule"
                        self.fixByRemove()
                    elif fixCode == "0":
                        print "Operation is Aborted"
                    break

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
