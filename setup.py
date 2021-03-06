# coding: utf-8

"""
    Safemat Api

    The Safemat REST API permits applications to connect securely to the Safemat software to carry out a multitude of operations.  Authentication and token-based access control is enforced.  ### Token: <table><thead><tr><th>Name</th><th>Token type</th><th>Lifetime</th></tr></thead><tbody><tr><td>Access token</td><td><a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://jwt.io/\">JWT</a>., Bearer token</td><td>60m</td></tr></tbody></table>  ### Access token usage  API requests (where authorisation is required) must include the bearer access token in the header.  Once the access token expires it should be refreshed.   ### How to determine if the token has expired <ol> <li>The API returns a 401 error.</li> <li>Check the <code>exp</code> field in the token payloads.</li> </ol>  ### Token structure  <table><thead><tr><th>Key name</th><th>Description</th></tr></thead><tbody><tr><td>exp</td><td>Expiration date and time in UNIX format</td></tr><tr><td>uid</td><td>Token owner(Unique number of devices(terminal))</td></tr><tr><td>terminal_id</td><td>Id in base of devices(terminal`s)</td></tr><tr><td>iat</td><td>Created date and time in UNIX format</td></tr></tbody></table>    # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Safemat Api",
    author_email="",
    url="",
    keywords=["Swagger", "Safemat Api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Safemat REST API permits applications to connect securely to the Safemat software to carry out a multitude of operations.  Authentication and token-based access control is enforced.  ### Token: &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Token type&lt;/th&gt;&lt;th&gt;Lifetime&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Access token&lt;/td&gt;&lt;td&gt;&lt;a rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://jwt.io/\&quot;&gt;JWT&lt;/a&gt;., Bearer token&lt;/td&gt;&lt;td&gt;60m&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;  ### Access token usage  API requests (where authorisation is required) must include the bearer access token in the header.  Once the access token expires it should be refreshed.   ### How to determine if the token has expired &lt;ol&gt; &lt;li&gt;The API returns a 401 error.&lt;/li&gt; &lt;li&gt;Check the &lt;code&gt;exp&lt;/code&gt; field in the token payloads.&lt;/li&gt; &lt;/ol&gt;  ### Token structure  &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Key name&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;exp&lt;/td&gt;&lt;td&gt;Expiration date and time in UNIX format&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;uid&lt;/td&gt;&lt;td&gt;Token owner(Unique number of devices(terminal))&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;terminal_id&lt;/td&gt;&lt;td&gt;Id in base of devices(terminal&#x60;s)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;iat&lt;/td&gt;&lt;td&gt;Created date and time in UNIX format&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;    # noqa: E501
    """
)
