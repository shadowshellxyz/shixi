from jd.api.base import RestApi

class YsdkMemberApplyJsfServiceQueryMemberStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.requestId = None
			self.platformCode = None

		def getapiname(self):
			return 'jingdong.ysdk.MemberApplyJsfService.queryMemberStatus'

			





