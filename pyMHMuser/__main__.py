# MHMuser - UserBot
# Copyright (C) 2021-2022 MHMuser
#
# This file is a part of < https://github.com/Dev-MHM/pyMHMuser/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/Dev-MHM/pyMHMuser/blob/main/LICENSE>.

import os
import sys
import time

from . import *
from .functions.helper import time_formatter, updater
from .startup.funcs import autopilot, customize, plug, ready, startup_stuff
from .startup.loader import load_other_plugins

# Option to Auto Update On Restarts..
if (
    udB.get_key("UPDATE_ON_RESTART")
    and os.path.exists(".git")
    and mhmuser_bot.run_in_loop(updater())
):
    os.system("git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "pyMHMuser")

startup_stuff()


mhmuser_bot.me.phone = None
mhmuser_bot.first_name = mhmuser_bot.me.first_name

if not mhmuser_bot.me.bot:
    udB.set_key("OWNER_ID", mhmuser_bot.uid)


LOGS.info("Initialising...")


mhmuser_bot.run_in_loop(autopilot())

pmbot = udB.get_key("PMBOT")
manager = udB.get_key("MANAGER")
addons = udB.get_key("ADDONS") or Var.ADDONS
vcbot = udB.get_key("VCBOT") or Var.VCBOT

load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

suc_msg = """
            ----------------------------------------------------------------------
                Ultroid has been deployed! Visit @MHMuser for updates!!
            ----------------------------------------------------------------------
"""

# for channel plugins
plugin_channels = udB.get_key("PLUGIN_CHANNEL")

# Customize Ultroid Assistant...
mhmuser_bot.run_in_loop(customize())

# Load Addons from Plugin Channels.
if plugin_channels:
    mhmuser_bot.run_in_loop(plug(plugin_channels))

# Send/Ignore Deploy Message..
if not udB.get_key("LOG_OFF"):
    mhmuser_bot.run_in_loop(ready())

cleanup_cache()

if __name__ == "__main__":
    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •ULTROID•"
    )
    LOGS.info(suc_msg)
    asst.run()
