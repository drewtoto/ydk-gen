#  ----------------------------------------------------------------
# Copyright 2018 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

"""netconf_provider.py
NetconfServiceProvider Python wrapper.
"""

from ydk.providers import NetconfServiceProvider as _NetconfServiceProvider


class NetconfServiceProvider(object):
    """ Python wrapper for NetconfServiceProvider
    """

    def __init__(self, address, username, password=None, port=830, protocol="ssh",
                       on_demand=True, common_cache=False, timeout=None, repo=None, private_key_path=None, public_key_path=None):

        if timeout is None:
            timeout = -1
        if port is None:
            port = 830
        if private_key_path is None:
            private_key_path = ""
        if public_key_path is None:
            public_key_path = ""

        if repo is None:
            if len(public_key_path) == 0:
                self.nsp = _NetconfServiceProvider(address, username, password, port,
                                                   protocol, on_demand, common_cache, timeout)
            else:
                self.nsp = _NetconfServiceProvider(address, username,
                                                   private_key_path, public_key_path,
                                                   port, on_demand, common_cache, timeout)
        else:
            if len(public_key_path) == 0:
                self.nsp = _NetconfServiceProvider(repo, address, username, password,
                                                   port, protocol, on_demand, timeout)
            else:
                self.nsp = _NetconfServiceProvider(repo, address, username,
                                                   private_key_path, public_key_path,
                                                   port, on_demand, timeout)

    def get_encoding(self):
        return self.nsp.get_encoding()

    def get_session(self):
        return self.nsp.get_session()

    def get_capabilities(self):
        return self.nsp.get_capabilities()
