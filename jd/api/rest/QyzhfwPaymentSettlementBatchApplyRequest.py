from jd.api.base import RestApi

class QyzhfwPaymentSettlementBatchApplyRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.requestJson = None

		def getapiname(self):
			return 'jingdong.qyzhfw.payment.settlementBatchApply'

			





