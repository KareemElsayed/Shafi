#!/usr/bin/python
#add virtual host  python program

from os.path import exists
from os import makedirs
from os import symlink
from os import system
from os import path

MAINDIRECTORY = '/var/www'

def createVirtualHost():
    createMainDirectory ()
    serverName= servername_valid ( MAINDIRECTORY )
    createIndexHtml ( serverName , MAINDIRECTORY )
    creatVirtualHostFiles ( serverName )
    linkToAccessAvailableSites ( serverName )
    path_file = '%s/%s' % ( MAINDIRECTORY , serverName )
    createconfigurationFile ( path_file , serverName )
    createBetweenAvailableAndEnableSites ( serverName )
    addIpDomainName ( serverName )
    restart_apache ( serverName )
    print("###########################################################")
    print("complete!!!!")

#to create /var/www if not exist

def createMainDirectory():
    system ( 'mkdir -p ' + MAINDIRECTORY )
    system ( 'chmod 755 '+ MAINDIRECTORY )
    return True    

# to create DocumentRoot

def createDocumentRoot ( serverName ):
     makedirs ( '%s/%s' % ( MAINDIRECTORY , serverName ))
     print ( "DocumentRoot is created" )
     return True

# to check the name of server to create it
    
def servername_valid( MAINDIRECTORY ):
    while True:
        serverName = raw_input ( "please enter the domain name:" )
        if exists ( '%s/%s'  %  ( MAINDIRECTORY , serverName )) or exists( '/etc/httpd/sites-available/%s.conf' % serverName ):
            print ( "this is name already exists.....>aborting" )

        else:
            createDocumentRoot (serverName)
            break
    return serverName
     

#to create index.html

def createIndexHtml ( serverName , MAINDIRECTORY ):
    d = path.join ( MAINDIRECTORY , serverName )
    indexPage = 'index.html'
    path_file = path.join( d , indexPage )
    data = open ( path_file , 'w' )
    print "index.html is created"
    success = writeIndexHtml ( data , serverName , path_file )
    if success:
        print "contents are written in index.html "	
    
    return True


#to write contents of index.html

def writeIndexHtml ( data , serverName , path_file ):
    data.write ( "<html>\n" )
    data.write ( "\t<head>\n" )
    data.write ( "\t\t<title>index</title>\n" )
    data.write ( "\t</head>\n" )
    data.write ( "\t<body>\n" )
    data.write ( "\t\t<h1>ServerName : "  +  serverName  +  " </h1>\n" )
    data.write ( "\t\t<h1>Location   : "  +  path_file  +  " </h1>\n" )
    data.write ( "\t</body>\n" )
    data.write ( "</html>\n" )
    data.close ()
    
    return True
    
#create Virtual Host Files if are not exist 

def creatVirtualHostFiles ( serverName ) :
    system ( 'mkdir -p /etc/httpd/sites-available' )
    system ( 'mkdir -p /etc/httpd/sites-enabled' )
    return True
    

#add the line in main configuration(httpd) to access configration of available sites       

def linkToAccessAvailableSites ( serverName ):
    print ( "write the line in main configuration to access configration of available sites " )
    line1 = system( 'cat /etc/httpd/conf/httpd.conf | grep sites-enabled' )
    line2 = 'Include sites-enabled/*.conf'
    if line1 == 256:      #line1 is equal 256 if line not exist and is equal zero if line exist
        mcf = open ( '/etc/httpd/conf/httpd.conf','a' )
        mcf.write ( line2 )
        mcf.close()
    return True

#to create configuration in the file that exist in sites-available

def createconfigurationFile ( path_file , serverName ):
        data = open ( '/etc/httpd/sites-available/%s.conf' % serverName , 'w' )
        indexPage = 'index.html'
        writeConfiguration ( data , path_file , serverName , indexPage  ) 
        data.close()
        return True
            
#this is function that write conf of virtual host in sites available 

def writeConfiguration ( data , path_file , serverName , indexPage ):
    data.write( "<VirtualHost *:80>\n" )
    data.write( "\tServerName " + serverName + "\n" )
    data.write( "\tDocumentRoot " + path_file + "\n" )
    data.write( "\tDirectoryIndex " + indexPage + "\n" )
    data.write( "\tErrorLog " + path_file + "/error.log\n" )
    data.write( "\tCustomLog " + path_file + "/access.log combined\n" )
    data.write( "</VirtualHost>" )
    print ( "configuration---->write" )
    return True 
    
#this function do link between enable and available sites
        
def createBetweenAvailableAndEnableSites ( serverName ):
    availableLink = '/etc/httpd/sites-available/%s.conf' % serverName
    enableLink = '/etc/httpd/sites-enabled/%s.conf' % serverName
    symlink(availableLink,enableLink)
    return True

#to add ip of domain name

def addIpDomainName ( serverName ):
    hosts = open ( '/etc/hosts' , 'a' )
    hosts.write ( '127.0.0.1' + '  ' + serverName + '\n' )
    print ( "add id to your domain name" )
    hosts.close()
    return True

#to restart apache server

def restart_apache ( serverName ):
    system ( 'service httpd restart' ) 
    print ( "restarting apache server" )
    print ( "success---->add your virtual host" )
    print ( "to delete your virtual host just run---> delVH.py" )
    indexPage = 'index.html'
    requestIndexPage ( serverName , indexPage )
    return True


def requestIndexPage ( serverName , indexPage ):	
	pass

#calling
    
createVirtualHost()


