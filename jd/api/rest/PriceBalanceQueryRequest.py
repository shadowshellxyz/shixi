from jd.api.base import RestApi

class PriceBalanceQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.payType = None

		def getapiname(self):
			return 'biz.price.balance.query'

		def get_version(self):
			return '1.0'
			
	




