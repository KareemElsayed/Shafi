#!/usr/bin/python
#delete virtual host  python program

from os import remove
from os.path import exists
from os import path
from os import system
from os import listdir
from os import rmdir

MAINDIRECTORY='/var/www/'

#to delete all files in virtual host 

def deleteVH ():
    show_list ()
    serverName = knowNameServer()
    deleteConfigurationFiles (serverName)
    DocumentRoot = path.join ( MAINDIRECTORY , serverName )
    removeVirtualHost ( DocumentRoot )
    deleteipDomainName(serverName)


#show the domain names in MainDirectory

def show_list ():
    system ( 'ls -l /var/www' )
    print ( "choose the domain name that you want to delete it!!!" )

#to know the name of Domain Name

def knowNameServer () :
    serverName = raw_input ( "please enter the domain name that you want to delete it:\n" )
    return serverName
 
# to delete configuration files of domain server

def deleteConfigurationFiles ( serverName ):
    configurationFile1 = '/etc/httpd/sites-available/'
    configurationFile2 = '/etc/httpd/sites-enabled/' 

    try:
        remove ( path.join ( configurationFile1 , '%s.conf' % serverName ) )
        print '%s.conf' % serverName , "exist in sites-available---->deleted"
        remove ( path.join ( configurationFile2 , '%s.conf' % serverName ) )
        print '%s.conf' % serverName , "exist in sites-enabled---->deleted"
 
    except:
         print ("there are not configurtion file of this domain")
   
    return True 



#to delete the directory of VH in document Root(i.e --->/var/www/yoursite)

def removeVirtualHost ( d ):

    while True:
        if exists ( d ):
            if not listdir ( d ):
                rmdir ( d )
                print '%s' % d ,"---->deleted"
            else:
                for f in listdir ( d ):
                    file_path = path.join ( d , f )
                    if path.isfile ( file_path ):
                        remove ( file_path )
                        print '%s' % f,"------->deleted"
                    elif path.isdir ( file_path ):
                        removeVirtualHost ( file_path )
        else:
            break
 
    return True
    
   
#to delete ip from hosts file

def deleteipDomainName ( serverName ):
    p1 = '/etc/hosts'
    p2 = '/etc/hhh'
    h = open ( p1 , 'r' )
    out = open ( p2 , 'w' )
    for line in h:
        if serverName not in line.split():
            out.write ( line )
       
    h.close()
    out.close()
    completeDelete ( p1 , p2 , serverName )
    return True

def completeDelete ( p1 , p2 , serverName ):
    h = open(p1,'w')
    out = open(p2,'r')
    for line in out:
        h.write ( line )
    h.close()
    out.close() 
    remove ( p2 ) 
    print "ip of Domain Name for ",'%s' % serverName,"------deleted from hosts file"
    print "######################################################################"
    print "complete!!!!"

#calling

deleteVH()

