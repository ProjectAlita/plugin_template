#   Copyright 2022 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" Module """
from pylon.core.tools import log, web  # pylint: disable=E0611,E0401
from pylon.core.tools import module  # pylint: disable=E0611,E0401

from .init_db import init_db

from ..shared.utils.api_utils import add_resource_to_api
from ..shared.utils.render import render_template_base


class Module(module.ModuleModel):
    """ Pylon module """

    def __init__(self, context, descriptor):
        self.context = context
        self.descriptor = descriptor

    def init(self):
        """ Init module """
        log.info(f'Initializing module {self.descriptor.name}')

        init_db()

        # blueprint endpoints
        self.descriptor.init_blueprint()

        # rpc functions
        self.init_rpc()

        # api
        self.init_api()

        # slots
        self.init_slots()

    def init_rpc(self):
        # self.context.rpc_manager.register_function(
        #     lambda: f'{self.descriptor.name} says hello!',
        #     name=f'hello_from_{self.descriptor.name}'
        # )

        ...

    def init_api(self):
        # add_resource_to_api(
        #     self.context.api,
        #     your_func,
        #     '/your/rule/1',
        #     '/your/rule/2',
        # )

        ...

    def init_slots(self):
        # self.context.slot_manager.register_callback('you_slot_name', your_slot_function)
        ...

    def deinit(self):  # pylint: disable=R0201
        """ De-init module """
        log.info(f'De-initializing module {self.descriptor.name}')

    @web.route('/')
    def index(self):
        # return render_template_base(
        #     'my_plugin:template.html',
        #     config={'some': 'data'}
        # )
        ...
