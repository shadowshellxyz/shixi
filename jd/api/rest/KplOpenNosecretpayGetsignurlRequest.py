from jd.api.base import RestApi

class KplOpenNosecretpayGetsignurlRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.req = None
			self.ptKey = None

		def getapiname(self):
			return 'jd.kpl.open.nosecretpay.getsignurl'

		def get_version(self):
			return '1.0'
			
	

class Req(object):
		def __init__(self):
			"""
			"""
			self.deviceId = None
			self.returnUrl = None
			self.macAddress = None
			self.imei = None
			self.appType = None





