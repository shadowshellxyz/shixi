from jd.api.base import RestApi

class NewWareAttributeValuesQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None

		def getapiname(self):
			return 'jingdong.new.ware.AttributeValues.query'

			





