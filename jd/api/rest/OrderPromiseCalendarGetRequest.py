from jd.api.base import RestApi

class OrderPromiseCalendarGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.province = None
			self.city = None
			self.county = None
			self.town = None
			self.paymentType = None
			self.sku = None

		def getapiname(self):
			return 'biz.order.promise.calendar.get'

		def get_version(self):
			return '1.0'
			
	

class SkuVo(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.num = None





