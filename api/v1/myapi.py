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

""" API """

from pylon.core.tools import log  # pylint: disable=E0611,E0401,W0611

from tools import api_tools, auth, config as c  # pylint: disable=E0401


class DefaultAPI(api_tools.APIModeHandler):  # pylint: disable=R0903
    """
        API Resource

        Endpoint URL structure: <pylon_root>/api/<api_version>/<plugin_name>/<resource_name>

        Example:
        - Pylon root is at "https://example.com/"
        - Plugin name is "demo"
        - We are in subfolder "v1"
        - Current file name is "myapi.py"

        API URL: https://example.com/api/v1/demo/myapi

        API resources use check_api auth decorator
        auth.decorators.check_api takes the following arguments:
        - permissions
        - scope_id=1
        - access_denied_reply={"ok": False, "error": "access_denied"},
    """

    # @auth.decorators.check_api({
    #     "permissions": ["models.plugin_template.myapi.get"],
    #     "recommended_roles": {
    #         c.ADMINISTRATION_MODE: {"admin": True, "editor": True, "viewer": False},
    #         c.DEFAULT_MODE: {"admin": True, "editor": True, "viewer": False},
    #     },
    # })
    # @api_tools.endpoint_metrics
    # def post(self, project_id: int, arg1: str | None = None):  # pylint: disable=R0201
    #     """ Process POST """
    #     # data = flask.request.json
    #     # ...
    #     return {"ok": True, "mydata": 42}


class API(api_tools.APIBase):
    url_params = api_tools.with_modes([
        '<int:project_id>',
        '<int:project_id>/<string:arg1>',
    ])

    mode_handlers = {
        c.DEFAULT_MODE: DefaultAPI
    }