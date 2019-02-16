#!/usr/bin/env python3
from scrap_cacher import app
import os
ip = os.environ.get("SERVER_IP", "0.0.0.0")
port = os.environ.get("PORT", 8000)
app.run(host = ip, port = port)
