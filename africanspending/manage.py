from flask.ext.script import Manager
from flask.ext.assets import ManageAssets

from africanspending.app import assets
from africanspending.views import app

manager = Manager(app)
manager.add_command("assets", ManageAssets(assets))

if __name__ == "__main__":
    manager.run()
