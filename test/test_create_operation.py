# coding: utf-8

"""
    Safemat Api

    The Safemat REST API permits applications to connect securely to the Safemat software to carry out a multitude of operations.  Authentication and token-based access control is enforced.  ### Token: <table><thead><tr><th>Name</th><th>Token type</th><th>Lifetime</th></tr></thead><tbody><tr><td>Access token</td><td><a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://jwt.io/\">JWT</a>., Bearer token</td><td>60m</td></tr></tbody></table>  ### Access token usage  API requests (where authorisation is required) must include the bearer access token in the header.  Once the access token expires it should be refreshed.   ### How to determine if the token has expired <ol> <li>The API returns a 401 error.</li> <li>Check the <code>exp</code> field in the token payloads.</li> </ol>  ### Token structure  <table><thead><tr><th>Key name</th><th>Description</th></tr></thead><tbody><tr><td>exp</td><td>Expiration date and time in UNIX format</td></tr><tr><td>uid</td><td>Token owner(Unique number of devices(terminal))</td></tr><tr><td>terminal_id</td><td>Id in base of devices(terminal`s)</td></tr><tr><td>iat</td><td>Created date and time in UNIX format</td></tr></tbody></table>    # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.create_operation import CreateOperation  # noqa: E501
from swagger_client.rest import ApiException


class TestCreateOperation(unittest.TestCase):
    """CreateOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateOperation(self):
        """Test CreateOperation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.create_operation.CreateOperation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
