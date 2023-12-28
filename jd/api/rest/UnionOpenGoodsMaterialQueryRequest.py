from jd.api.base import RestApi

class UnionOpenGoodsMaterialQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsReq = None

		def getapiname(self):
			return 'jd.union.open.goods.material.query'

		def get_version(self):
			return '1.0'
			
	

class GoodsReq(object):
		def __init__(self):
			"""
			"""
			self.eliteId = None
			self.pageIndex = None
			self.pageSize = None
			self.sortName = None
			self.sort = None
			self.pid = None
			self.subUnionId = None
			self.siteId = None
			self.positionId = None
			self.ext1 = None
			self.skuId = None
			self.hasCoupon = None
			self.userIdType = None
			self.userId = None
			self.fields = None
			self.forbidTypes = None
			self.orderId = None
			self.groupId = None
			self.ownerUnionId = None
			self.benefitType = None





