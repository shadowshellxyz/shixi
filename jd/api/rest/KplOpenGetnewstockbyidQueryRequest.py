from jd.api.base import RestApi

class KplOpenGetnewstockbyidQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuNums = None
			self.area = None

		def getapiname(self):
			return 'jd.kpl.open.getnewstockbyid.query'

		def get_version(self):
			return '1.0'
			
	

class StockVo(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.num = None





