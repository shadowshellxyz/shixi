from jd.api.base import RestApi

class UserGetUserInfoByOpenIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.openId = None

		def getapiname(self):
			return 'jingdong.user.getUserInfoByOpenId'

			





