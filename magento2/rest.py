# coding: utf-8
try:
    import requests
    import json
except ImportError:
    pass


class Client(object):

    def __init__(self, url, token, verify_ssl=True):
        self._url = url
        self._token = token
        self._verify_ssl = verify_ssl

    def login(self, username, password):
        """
        Fetches Token for further identification
        :param username:
        :param password:
        :return:
        """
        url = '%s/%s' % (self._url, "integration/admin/token")
        payload = json.dumps({
            'username': username,
            'password': password
        })
        headers = {
            "Content-Type": "application/json"
        }
        # TODO: Add Error Handling here if not status=200 OK !
        token = requests.post(
            url, data=payload, verify=self._verify_ssl, headers=headers)
        self._token = json.loads(token.text)

    def get(self, resource_path, arguments):
        url = '%s/%s' % (self._url, resource_path)
        res = requests.get(
            url, params=arguments, verify=self._verify_ssl,
            headers={'Authorization': 'Bearer %s' % self._token})
        res.raise_for_status()
        return res.json()

    def post(self, resource_path, arguments):
        url = '%s/%s' % (self._url, resource_path)
        res = requests.post(
            url, data=json.dumps(arguments), verify=self._verify_ssl,
            headers={'Authorization': 'Bearer %s' % self._token, "Content-Type": "application/json"})
        res.raise_for_status()
        return res.json()

    def put(self, resource_path, arguments):
        url = '%s/%s' % (self._url, resource_path)
        res = requests.put(
            url, params=arguments, verify=self._verify_ssl,
            headers={'Authorization': 'Bearer %s' % self._token})
        res.raise_for_status()
        return res.json()

    def delete(self, resource_path, arguments):
        url = '%s/%s' % (self._url, resource_path)
        res = requests.delete(
            url, params=arguments, verify=self._verify_ssl,
            headers={'Authorization': 'Bearer %s' % self._token})
        res.raise_for_status()
        return res.json()

    def patch(self, resource_path, arguments):
        url = '%s/%s' % (self._url, resource_path)
        res = requests.patch(
            url, params=arguments, verify=self._verify_ssl,
            headers={'Authorization': 'Bearer %s' % self._token})
        res.raise_for_status()
        return res.json()
