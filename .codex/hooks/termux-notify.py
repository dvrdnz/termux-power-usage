#!/usr/bin/env python3
import json
import shlex
import subprocess
import sys

try:
    event = json.loads(sys.argv[1])
except (IndexError, json.JSONDecodeError):
    event = {}

thread_id = event.get("thread-id")
message = event.get(
    "last-assistant-message",
    "Codex notification"
)

message = " ".join(str(message).split())[:500]

if thread_id:
    action = (
        f"codex queue --thread {shlex.quote(thread_id)} "
        f'--message "$REPLY"'
    )
else:
    action = "termux-toast 'Codex thread-id missing'"

subprocess.run(
    [
        "termux-notification",
        "--title", "Codex CLI",
        "--content", message,
        "--id", "codex-cli",
        "--priority", "high",
        "--button1", "Prompt",
        "--button1-action", action,
        "--type", "basic",
    ],
    check=False,
)
