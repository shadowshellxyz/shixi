from jd.api.base import RestApi

class KplOpenMigumusicCheckstatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.dataJson = None

		def getapiname(self):
			return 'jd.kpl.open.migumusic.checkstatus'

		def get_version(self):
			return '1.0'
			
	




