#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from configobj import ConfigObj
from flask_script import Command, Manager, Option

from tilty_dashboard import app
from tilty_dashboard.controller import start_webapp

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class GunicornServer(Command):
    """Run the webserver in gunicorn."""
    def get_options(self):
        from gunicorn.config import make_settings
        settings = make_settings()
        options = []
        for setting, klass in settings.items():
            if klass.cli:
                if klass.const is not None:
                    options.append(
                        Option(
                            *klass.cli,
                            const=klass.const,
                            action=klass.action
                        )
                    )
                else:
                    options.append(Option(*klass.cli, action=klass.action))
        return options

    def run(self, *args, **kwargs):
        from gunicorn.app.wsgiapp import WSGIApplication
        app = WSGIApplication()
        app.app_uri = 'manage:app'
        return app.run()


manager = Manager(app)

manager.add_command("gunicorn", GunicornServer())


@manager.command
def runserver(host="127.0.0.1", port="5000"):
    """Override default `runserver` to init webapp before running."""
    config = ConfigObj('config/dev.config', configspec='config/dev.configspec')
    start_webapp(config)


if __name__ == "__main__":
    manager.run()
