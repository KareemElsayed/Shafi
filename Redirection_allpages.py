import re

class Redirection :
    found           = 0
    temp            = 0
    port            = 443

    sslC1           = re.compile(r"SSLEngine on\s")
    sslC2           = re.compile(r"SSLCertificateFile\s")
    sslC3           = re.compile(r"SSLCertificateKeyFile\s")
    sslC4           = re.compile(r"Listen\s") # \s is whitespace
    sslC5           = re.compile(r"\sServerName\s") # \s is whitespace ""

    start           = "<VirtualHost *:80>"
    end             = "</VirtualHost>"

    rewriteC1       = re.compile(r"\sRewriteCond\s")
    rewriteC2       = re.compile(r"\sRewriteEngine\s")
    rewriteC3       = re.compile(r"\sRewriteRule\s")
    
    def __init__(self):
        readFile = open("conf.txt","r+")
        lines = readFile.readlines()
        readFile.seek(0)
        readFile.truncate()
        self.searchSSL(lines)
        self.searchRedir(lines)
        try :
            self.addRedir(lines)
        except :
            for line in lines :
                readFile.write(line)
        readFile.close()
    def searchSSL (self,lines):
        for line in lines :
            if line.startswith('#') == False :
                if bool(Redirection.sslC1.search(line)) :
                    Redirection.found += 1
                    print (line.strip())
                elif bool(Redirection.sslC2.search(line)) :
                    Redirection.found += 1
                    print (line.strip())
                elif bool(Redirection.sslC3.search(line)) :
                    Redirection.found += 1
                    print (line.strip())
                elif bool(Redirection.sslC4.search(line)) and str(Redirection.port) in line:
                    Redirection.found += 1
                    print (line.strip())
                elif bool(Redirection.sslC5.search(line)):
                    Redirection.found += 1
                    print (line.strip())
        print ("--------------------------------------------------")
                  

    def searchRedir (self,lines):
        for line in lines :
            if line.startswith('#') == False :
                if bool(Redirection.rewriteC1.search(line)) :
                    Redirection.temp +=1
                    print (line.strip())
                elif bool(Redirection.rewriteC2.search(line)) :
                    Redirection.temp +=1
                    print (line.strip())
                elif bool(Redirection.rewriteC3.search(line)) :
                    Redirection.temp +=1
                    print (line.strip())
        print ("---------------------------------------------------")  
               

    
    def addRedir (self,lines):
        readFile = open("conf.txt","r+")
        if Redirection.found == 5 and Redirection.temp < 3:
            for line in lines :
                readFile.write(line)
                if self.start in line.strip():
                    readFile.write("    RewriteEngine On\n")
                    readFile.write("    RewriteCond %{HTTPS} off\n")
                    readFile.write("    RewriteRule (.*) https://%{SERVER_NAME}/%$1 [R=301,L]\n")
            print("SSL COMMANDS FOUND")
    
        else :
            for line in lines:
                readFile.write(line)
        if Redirection.found != 5 :
            print("ERROR : SSL COMMANDS NOT FOUND")
        else :
            print ("REWRITE COMMANDS ALREADY EXIST")
        print ("SSL COMMANDS found = ",Redirection.found)
        print ("REWRITE COMMANDS found = ",Redirection.temp)
        readFile.close()

        
    
        















        
