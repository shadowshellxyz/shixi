from jd.api.base import RestApi

class KplOpenFalvwangRequestRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wrapJson = None

		def getapiname(self):
			return 'jd.kpl.open.falvwang.request'

		def get_version(self):
			return '1.0'
			
	




