from jd.api.base import RestApi

class KeplerServicePromotionGoodsinfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuIds = None

		def getapiname(self):
			return 'jd.kepler.service.promotion.goodsinfo'

		def get_version(self):
			return '1.0'
			
	




