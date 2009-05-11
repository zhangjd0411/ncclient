# Copyright 2009 Shikhar Bhushan
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

"TODO: docstrings"

from ncclient.errors import TransportError

class AuthenticationError(TransportError):
    pass

class SessionCloseError(TransportError):
    
    def __init__(self, in_buf, out_buf=None):
        msg = 'Unexpected session close.'
        if in_buf:
            msg += ' IN_BUFFER: {%s}' % in_buf
        if out_buf:
            msg += ' OUT_BUFFER: {%s}' % out_buf
        SSHError.__init__(self, msg)

class SSHError(TransportError):
    pass

class SSHUnknownHostError(SSHError):
    
    def __init__(self, hostname, key):
        from binascii import hexlify
        SSHError(self, 'Unknown host key [%s] for [%s]'
                 % (hexlify(key.get_fingerprint()), hostname))
        self.hostname = hostname
