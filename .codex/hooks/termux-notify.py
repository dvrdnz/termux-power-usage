#!/usr/bin/env python3
import json
import subprocess
import sys

try:
    event = json.loads(sys.argv[1])
except (IndexError, json.JSONDecodeError):
    event = {}

message = event.get(
    "last-assistant-message",
    "Codex notification"
)

message = " ".join(str(message).split())[:500]

subprocess.run(
    [
        "termux-notification",
        "--title", "Codex CLI",
        "--content", message,
        "--id", "codex-cli",
        "--priority", "high",
        "--type", "basic",
    ],
    check=False,
)
