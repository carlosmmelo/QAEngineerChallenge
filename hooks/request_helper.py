import logging

import requests
from conf.env_setup import EnvSetup


class RequestHelper(object):
	logger = logging.getLogger(__name__)

	@staticmethod
	def print_response_json(request):
		RequestHelper.logger.debug('Response code: %s', request.status_code)
		if request.status_code not in [204, 404]:
			RequestHelper.logger.debug(u'''Response json:
			{json}'''.format(json=request.json()))\


	@staticmethod
	def send_get_request():
		url = EnvSetup.API_HOST + EnvSetup.ENDPOINT
		RequestHelper.logger.debug(u'''Sending GET request
			URL  = {url}'''.format(url=url))
		response = requests.get(url)
		RequestHelper.print_response_json(response)
		return response
