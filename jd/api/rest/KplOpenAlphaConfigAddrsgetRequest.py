from jd.api.base import RestApi

class KplOpenAlphaConfigAddrsgetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ptKey = None
			self.ip = None

		def getapiname(self):
			return 'jd.kpl.open.alpha.config.addrsget'

		def get_version(self):
			return '1.0'
			
	




