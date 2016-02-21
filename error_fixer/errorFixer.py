from forbidden_access_fixer.apDenyRuleFixer import *
from forbidden_access_fixer.apPermissionDeniedFixer import *


def fixError(ed):
	if ed["errorTag"] == "deny rule":
		print("Iam Deny error")
	elif ed["errorTag"] == "permission denied":		
		fixPermissionError(ed["info"]["path"])
	else:
		print("unknown error")
