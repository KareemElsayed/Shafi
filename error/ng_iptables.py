import subprocess
from pprint import pprint


class NgIptables:
	
	a = {"INPUT" : {}, "FORWARD" : {}, "OUTPUT" : {}}
	iptables_rule = None
	def __init__(self):
		self.iptables_rule = subprocess.Popen(["iptables -L -n --line-number"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()

	def __addRule(self,chain,rules):
		for i in rules:
			if len(i) == 1 and i == "\n":
				break
			else:
				if i[0].isdigit():
					i = i.strip().split()
					self.a[chain][i[0]] = {"target"      : i[1],
						  	  "prot"        : i[2],
						  	  "opt"         : i[3],
						  	  "source"      : i[4],
						  	  "distination" : i[5],
						  	  "stat"        :  str(" ".join(i[6:])) if len(i) > 6 else None 	
						  	}
	def getRule(self):
		for i in self.iptables_rule:
        		if "INPUT" in i:
                		self.__addRule("INPUT"   , self.iptables_rule[self.iptables_rule.index(i):])
			if "FORWARD" in i:
				self.__addRule("FORWARD" , self.iptables_rule[self.iptables_rule.index(i):])
			if "OUTPUT" in i:
				self.__addRule("OUTPUT"  , self.iptables_rule[self.iptables_rule.index(i):])
		return self.a
rules = NgIptables()
a = rules.getRule()

for i in a["INPUT"]:
	if a["INPUT"][i]["target"] == "REJECT":
		print "------------- Rejected rule ------------"
		print a["INPUT"][i]
		print i
		print "------------ Rejected rule -------------"

x = raw_input("Do you want Disable rule ? [y/n] : ")
if str(x) == "y":	
	i = raw_input("Please Enter Number of Rule: ")
	subprocess.Popen(["iptables -D INPUT "+i], shell= True)
	print "Rule is Removed"
else:
	print "Thank you"



