import os , sys , stat 


#permission like 755 , 751 , 533 .... .(string)
#set the target=1 when it is a directory & target=2 when it is a file .(int)
def setTargetPermission(path,permissions,target): 
	try:
		ownerPermission = int(permissions[0])
		groupPermission = int(permissions[1])
		otherPermission = int(permissions[2])
		x = 0

		if ownerPermission == 7:
			x = x | stat.S_IRWXU
		elif ownerPermission == 6:
			x = x | stat.S_IREAD | stat.S_IWRITE
		elif ownerPermission == 5:
			x = x | stat.S_IREAD | stat.S_IEXEC
		elif ownerPermission == 4:
			x = x | stat.S_IREAD
		elif ownerPermission == 3:
			x = x | stat.S_IWRITE | stat.S_IEXEC
		elif ownerPermission == 2:
			x = x | stat.S_IWRITE
		elif ownerPermission == 1:
			x = x | stat.S_IEXEC
	
		if groupPermission == 7:
			x = x | stat.S_IRWXG
		elif groupPermission == 6:
			x = x | stat.S_IRGRP | stat.S_IWGRP
		elif groupPermission == 5:
			x = x | stat.S_IRGRP | stat.S_IXGRP
		elif groupPermission == 4:
			x = x | stat.S_IRGRP
		elif groupPermission == 3:
			x = x | stat.S_IWGRP | stat.S_IXGRP
		elif groupPermission == 2:
			x = x | stat.S_IWGRP
		elif groupPermission == 1:
			x = x | stat.S_IXGRP

		if otherPermission == 7:
			x = x | stat.S_IRWXO
		elif otherPermission == 6:
			x = x | stat.S_IROTH | stat.S_IWOTH
		elif otherPermission == 5:
			x = x | stat.S_IROTH | stat.S_IXOTH
		elif otherPermission == 4:
			x = x | stat.S_IROTH
		elif otherPermission == 3:
			x = x | stat.S_IWOTH | stat.S_IXOTH
		elif otherPermission == 2:
			x = x | stat.S_IWOTH
		elif otherPermission == 1:
			x = x | stat.S_IXOTH

		if target == 1:				#the target is a directory
			os.chmod(path, x)
		else:						#the target is a file
			fd = os.open( path , os.O_RDONLY )
			os.fchmod(fd, x)
			os.close( fd )
	except Exception:
		return False
	return True


#print(os.path.isfile("/var/www/html"))
#print(os.path.isfile("/var/www/html/"))


# change the permission of whole the path .. 755 for directory and 644 for files
def fixPermissionError(path):
	path = path.strip("/")
	ls = path.split("/")						
	for i in range(1,len(ls)+1):
		p = "/"+"/".join(ls[0:i])				#sub path  like -> /var - /var/www - /var/www/gpx/
		if os.path.isfile(p):					#if the generated path corresponds to a file 
			setTargetPermission(p,"644",2)
		else:									#if the generated path corresponds to a directory
			setTargetPermission(p,"755",1)
	print("shafi ....  fixed ...")
		
	







