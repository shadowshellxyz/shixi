from jd.api.base import RestApi

class KeplerSkuProductServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuIdSet = None
			self.extFieldSet = None

		def getapiname(self):
			return 'jd.kepler.sku.ProductService'

		def get_version(self):
			return '1.0'
			
	




