from jd.api.base import RestApi

class KplOpenAftersaleOrderidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.refId = None
			self.orderId = None

		def getapiname(self):
			return 'jd.kpl.open.aftersale.orderid'

		def get_version(self):
			return '1.0'
			
	




