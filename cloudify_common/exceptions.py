########
# Copyright (c) 2018 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


class NoContextSet(RuntimeError):
    """ Attempted accessing a context, but no context is available. """


class HTTPException(Exception):
    """"""
    def __init__(self, url, code, reason):
        self.url = url
        self.code = code
        self.reason = reason

    def __str__(self):
        return '{0} ({1}) : {2}'.format(self.code, self.url, self.reason)
