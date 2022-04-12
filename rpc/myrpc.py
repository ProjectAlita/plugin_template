#!/usr/bin/python3
# coding=utf-8

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

""" RPC """

from pylon.core.tools import log  # pylint: disable=E0611,E0401,W0611
from pylon.core.tools import web  # pylint: disable=E0611,E0401

from tools import db  # pylint: disable=E0401
from tools import db_tools  # pylint: disable=E0401
from tools import rpc_tools  # pylint: disable=E0401


class RPC:  # pylint: disable=E1101,R0903
    """
        RPC Resource

        self is pointing to current Module instance

        web.rpc decorator takes two arguments:
        - name=None -> RPC function name
        - proxy_name=None -> (optional) 'proxy' function name to create in current Module
        Note: web.rpc decorator must be the last decorator (at top)

        It is recommended to wrap all exceptions into "RuntimeError"

        RPCs do not support auth checks via auth decorators

    """


    @web.rpc("demo_do_smth", "do_smth")
    @rpc_tools.wrap_exceptions(RuntimeError)
    def _do_smth(self, key, default=...):
        try:
            with db.engine.connect() as connection:
                item = connection.execute(
                    self.db.tbl.demo.select().where(
                        self.db.tbl.demo.c.key == key,
                    )
                ).mappings().one()
            return db_tools.sqlalchemy_mapping_to_dict(item)["data"]
        except:  # pylint: disable=W0702
            if default is ...:
                default = dict()
            return default
