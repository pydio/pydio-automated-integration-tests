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
import pytest, json, logging

def inner_debug(message):
    logging.info("  | %s" % message)

@pytest.fixture
def server_def():
    server_file = 'configs/server.json'
    with open(server_file) as handler:
        jDict = json.load(handler)
    return jDict

@pytest.fixture
def workspaces_defs():
    repo_file = 'configs/workspaces.json'
    with open(repo_file) as handler:
        jDict = json.load(handler)
    return jDict

@pytest.fixture
def workspace_id(request):
    repo_file = 'configs/workspaces.json'
    with open(repo_file) as handler:
        workspaces_defs = json.load(handler)

    server_file = 'configs/server.json'
    with open(server_file) as handler:
        server_def = json.load(handler)

    from sdk.ajxp_conf import create_repo, delete_repo
    repo_id = create_repo(server_def, workspaces_defs[0])
    def fin():
        print ("teardown repo")
        delete_repo(server_def, repo_id)
    request.addfinalizer(fin)
    return repo_id