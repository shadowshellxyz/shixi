from jd.api.base import RestApi

class KplOpenConfirmreceivedQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None

		def getapiname(self):
			return 'jd.kpl.open.confirmreceived.query'

		def get_version(self):
			return '1.0'
			
	




