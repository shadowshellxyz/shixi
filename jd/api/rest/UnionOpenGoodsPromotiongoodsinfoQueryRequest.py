from jd.api.base import RestApi

class UnionOpenGoodsPromotiongoodsinfoQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuIds = None

		def getapiname(self):
			return 'jd.union.open.goods.promotiongoodsinfo.query'

		def get_version(self):
			return '1.0'
			
	




