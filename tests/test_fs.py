# coding=utf-8
#
# Copyright 2007-2014 Charles du Jeu - Abstrium SAS <team (at) pyd.io>
#  This file is part of Pydio.
#
#  Pydio is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pydio is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Pydio.  If not, see <http://www.gnu.org/licenses/>.
#
#  The latest code can be found at <http://pyd.io/>.
#
from configs.config_logger import setup_logging
from configs.commons import *
from sdk.ajxp_conf import *

setup_logging(logging.INFO)

def create_delete(sdk, path):
    # CREATE FILE
    sdk.mkfile(path)
    # CHECK FILE IS IN LIST
    result = sdk.list('/')
    inner_debug(result)
    assert path in result

    # DELETE FILE
    sdk.delete(path)
    # CHECK FILE IS NO MORE IN LIST
    result = sdk.list('/')
    inner_debug(result)
    assert path not in result


def test_fs(server_def, workspace_id):

    sdk = PydioSdk(server_def['host'], workspace_id, unicode(''), '', (server_def['user'], server_def['pass']))
    sdk.stick_to_basic = True

    #path = '/pydio-simple-file'
    create_delete(sdk, '/pydio-simple-file')
    create_delete(sdk, '/fichié accentué'.decode('utf-8'))