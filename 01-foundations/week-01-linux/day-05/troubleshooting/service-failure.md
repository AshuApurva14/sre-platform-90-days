# Service Failure Investigation

## Problem

`sre-demo.service` failed to start.

## Initial Check

```bash
systemctl status sre-demo

Logs
journalctl -u sre-demo -n 50
Finding

The ExecStart path pointed to a non-existent script.

Fix

Corrected the ExecStart configuration.

Reload
systemctl daemon-reload
Recovery
systemctl restart sre-demo
Verification
systemctl status sre-demo
journalctl -u sre-demo -n 20
Lesson Learned

