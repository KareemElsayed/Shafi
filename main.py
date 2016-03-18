from apErrorLogListener import *

#path = "/var/log/nginx/error.log"
path = "/var/log/apache2/error.log"



def main():
	eh = MyEventHandler(path)
	


if __name__ == '__main__':
	main()
	
