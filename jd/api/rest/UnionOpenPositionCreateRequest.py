from jd.api.base import RestApi

class UnionOpenPositionCreateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.positionReq = None

		def getapiname(self):
			return 'jd.union.open.position.create'

		def get_version(self):
			return '1.0'
			
	

class PositionReq(object):
		def __init__(self):
			"""
			"""
			self.unionId = None
			self.key = None
			self.unionType = None
			self.type = None
			self.spaceNameList = None
			self.siteId = None





