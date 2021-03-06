#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PassWebTool import parseParams, PassWebToolException, environ, sleep
from PassWebTool.PassWebToolClass import KpDbClass
from PassWebTool.Renderer import RenderCLI, RenderCGI

ui = RenderCLI()
if environ.has_key('HTTP_USER_AGENT'):
    ui = RenderCGI()
else:
    environ['REMOTE_ADDR'] = environ['USER']

try:
    opmode, config, e = parseParams()
    KpDb = KpDbClass(config)
    KpDb.open()
except PassWebToolException, e:
    ui.print_error(str(e))
    ui.quit()

if __name__ == '__main__':
    if e['pwid'] is None:
        ui.print_title("GET by PWID")
        e['pwid'] = ui.ask_pwid()

    if e['pwid'] is None:
        ui.quit()

    entry = KpDb.get_pwid(pwid=e['pwid'])

    sleep(config['delay_answer'])  # don't go too fast

    ui.print_entry(entry, mode=opmode)

