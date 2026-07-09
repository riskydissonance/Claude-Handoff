#!/usr/bin/env python3
"""Blocks Edit/Write/MultiEdit from the main session; subagent-issued edits pass through."""
import json, sys

data = json.load(sys.stdin)

# agent_type / agent_id are only populated when the call originates inside a subagent.
is_subagent = bool(data.get("agent_type") or data.get("agent_id"))

if is_subagent:
    sys.exit(0)  # allow — this is Worker (or another subagent) doing its job

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            "Main session cannot edit files directly. Delegate to the Worker "
            "subagent — batch any other pending small changes into the same call."
        )
    }
}))
sys.exit(2)
