from jd.api.base import RestApi

class KplOpenWareZhaoshangGoodsQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.kpl.open.ware.zhaoshang.goods.query'

			





