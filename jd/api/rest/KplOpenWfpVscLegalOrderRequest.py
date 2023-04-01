from jd.api.base import RestApi

class KplOpenWfpVscLegalOrderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.interfaceName = None
			self.methodName = None
			self.param = None

		def getapiname(self):
			return 'jd.kpl.open.wfp.vsc.legalOrder'

		def get_version(self):
			return '1.0'
			
	

class Param(object):
		def __init__(self):
			"""
			"""
			self.merchantCode = None
			self.data = None





