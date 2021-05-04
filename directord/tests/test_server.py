#   Copyright Peznauts <kevin@cloudnull.com>. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import unittest

from directord import server
from directord import tests


class TestServer(unittest.TestCase):
    def setUp(self):
        self.args = tests.FakeArgs()
        self.client = server.Server(args=self.args)

    def tearDown(self):
        pass

    def test_heartbeat_bind(self):
        pass

    def test_job_bind(self):
        pass

    def test_transfer_bind(self):
        pass

    def test_run_heartbeat(self):
        pass

    def test__run_transfer(self):
        pass

    def test_create_return_jobs(self):
        pass

    def test_run_job(self):
        pass

    def test_run_interactions(self):
        pass

    def test_run_socket_server(self):
        pass

    def test_worker_run(self):
        pass
