from jd.api.base import RestApi

class InvoiceWaybillRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.markId = None

		def getapiname(self):
			return 'biz.invoice.waybill'

		def get_version(self):
			return '1.0'
			
	




