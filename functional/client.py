__author__ = 'ekonstantinov'
import requests
from json import dumps
import time


class TestingAdapterClient(object):
    def __init__(self, url):
        self.url = url

    def _request(self, method, url, data=None):
        headers = {'content-type': 'application/json'}
        if data:
            print data
        r = requests.request(method, url, data=data, headers=headers, timeout=30.0)
        if 2 != r.status_code/100:
            raise AssertionError('{method} "{url}" responded with "{code}" status code'
                                    .format(method=method.upper(), url=url, code=r.status_code))
        return r

    def __getattr__(self, item):
        getters = ['testsets', 'tests', 'testruns']
        if item in getters:
            url = ''.join([self.url, '/', item])
            return lambda: self._request('GET', url)

    def testruns_last(self, cluster_id):
        url = ''.join([self.url, '/testruns/last/',
                       str(cluster_id)])
        return self._request('GET', url)

    def start_testrun(self, testset, cluster_id):
        return self.start_testrun_tests(testset, [], cluster_id)

        '''url = ''.join([self.url, '/testruns'])
        data = [{'testset': testset,
                'metadata': {'cluster_id': str(cluster_id)}}]

        return self._request('POST', url, data=dumps(data))'''

    def start_testrun_tests(self, testset, tests, cluster_id):
        url = ''.join([self.url, '/testruns'])
        data = [{'testset': testset,
                 'tests': tests,
                 'metadata': {'cluster_id': str(cluster_id)}}]
        return self._request('POST', url, data=dumps(data))

    def stop_testrun(self, testrun_id):
        url = ''.join([self.url, '/testruns'])
        data = [{"id": testrun_id,
                 "status": "stopped"}]
        return self._request("PUT", url, data=dumps(data))

    def stop_testrun_last(self, testset, cluster_id):
        latest = self.testruns_last(cluster_id).json()
        testrun_id = [item['id'] for item in latest if item['testset'] == testset][0]
        return self.stop_testrun(testrun_id)

    def restart_tests(self, tests, testrun_id):
        url = ''.join([self.url, '/testruns'])
        body = [{'id': str(testrun_id),
                 'tests': tests,
                 'status': 'restarted'}]
        return self._request('PUT', url, data=dumps(body))

    def restart_tests_last(self, testset, tests, cluster_id):
        latest = self.testruns_last(cluster_id).json()
        testrun_id = [item['id'] for item in latest if item['testset'] == testset][0]
        return self.restart_tests(tests, testrun_id)

    def _with_timeout(self, action, testset, cluster_id, timeout):
        start_time = time.time()
        json = action().json()

        if json == [{}]:
            self.stop_testrun_last(testset, cluster_id)
            time.sleep(1)
            action()

        while time.time() - start_time <= timeout:
            time.sleep(5)

            current_response = self.testruns_last(cluster_id)
            current_status = [item['status'] for item in current_response.json()
                              if item['testset'] == testset][0]

            if current_status == 'finished':
                break
        else:
            current_response = self.stop_testrun_last(testset, cluster_id)

        return current_response

    def run_with_timeout(self, testset, tests, cluster_id, timeout):
        action = lambda: self.start_testrun_tests(testset, tests, cluster_id)
        return self._with_timeout(action, testset, cluster_id, timeout)

    def restart_with_timeout(self, testset, tests, cluster_id, timeout):
        action = lambda: self.restart_tests_last(testset, tests, cluster_id)
        return self._with_timeout(action, testset, cluster_id, timeout)



