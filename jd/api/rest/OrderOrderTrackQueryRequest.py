from jd.api.base import RestApi

class OrderOrderTrackQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None

		def getapiname(self):
			return 'biz.order.orderTrack.query'

		def get_version(self):
			return '1.0'
			
	




