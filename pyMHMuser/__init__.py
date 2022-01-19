# MHMuser - UserBot
# Copyright (C) 2021-2022 MHMuser
#
# This file is a part of < https://github.com/Dev-MHM/pyMHMuser/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/Dev-MHM/pyMHMuser/blob/main/LICENSE>.

import time

from .configs import Var
from .startup import *
from .startup._database import UltroidDB
from .startup.BaseClient import MHMClient
from .startup.connections import session_file, vc_connection, where_hosted
from .startup.funcs import _version_changes, autobot
from .version import ultroid_version

start_time = time.time()
_ult_cache = {}
# sys.exit = sys_exit()
HOSTED_ON = where_hosted()

udB = UltroidDB()

LOGS.info(f"Connecting to {udB.name}...")
if udB.ping():
    LOGS.info(f"Connected to {udB.name} Successfully!")

BOT_MODE = udB.get_key("BOTMODE")
DUAL_MODE = udB.get_key("DUAL_MODE")

if BOT_MODE:
    if DUAL_MODE:
        udB.del_key("DUAL_MODE")
        DUAL_MODE = False
    mhmuser_bot = None
else:
    mhmuser_bot = MHMClient(
        session_file(LOGS),
        udB=udB,
        app_version=ultroid_version,
        device_model="Ultroid",
        proxy=udB.get_key("TG_PROXY"),
    )

if not BOT_MODE:
    mhmuser_bot.run_in_loop(autobot())
else:
    if not udB.get_key("BOT_TOKEN") and Var.BOT_TOKEN:
        udB.set_key("BOT_TOKEN", Var.BOT_TOKEN)
    if not udB.get_key("BOT_TOKEN"):
        LOGS.info('"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"')
        import sys

        sys_exit()

asst = MHMClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

if BOT_MODE:
    mhmuser_bot = asst

vcClient = vc_connection(udB, mhmuser_bot)

_version_changes(udB)

HNDLR = udB.get_key("HNDLR") or "."
DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
