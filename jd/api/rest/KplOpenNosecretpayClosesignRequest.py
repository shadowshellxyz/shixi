from jd.api.base import RestApi

class KplOpenNosecretpayClosesignRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deviceId = None
			self.ptKey = None

		def getapiname(self):
			return 'jd.kpl.open.nosecretpay.closesign'

		def get_version(self):
			return '1.0'
			
	




