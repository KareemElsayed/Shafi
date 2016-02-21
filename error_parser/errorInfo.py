from forbidden_access_parser.apDenyRuleParser import *
from forbidden_access_parser.apPermissionDeniedParser import *


def getErrorInfo(errorLine):


	if isApPermissionDenied(errorLine):
		return getApPermissionDeniedInfo(errorLine)
	elif isError(errorLine):
		return DenyRule(errorLine).parseforbiddenAccess()
	else:
		return {}

