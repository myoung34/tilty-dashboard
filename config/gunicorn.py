#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configobj import ConfigObj

from tilty_dashboard import init_webapp

configobj_path = 'config/dev.config'

configobj = ConfigObj(
    configobj_path,
    configspec=f'{configobj_path}spec',
)
host = configobj['webapp']['host']
port = configobj['webapp']['port']
bind = f'{host}:{port}'
log_level = 'info'
accesslog = '-'
errorlog = '-'
capture_output = True


def on_starting(server):
    server.log.setup(server.app.cfg)
    server.app.configobj = configobj


def post_fork(server, worker):
    init_webapp(server.app.configobj)
