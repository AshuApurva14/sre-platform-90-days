# Week 01 — Linux Foundations

## Objective

Build a practical understanding of Linux required for DevOps and SRE work.

## Topics

* Linux command line
* Files and directories
* Users and groups
* File permissions
* Processes
* PIDs and PPIDs
* Signals
* Background/foreground processes
* Services
* systemd
* Logs
* Bash scripting
* Text processing
* Basic troubleshooting

## Resource

Linux Foundation — Introduction to Linux (LFS101)

It is currently offered as free, self-paced material and includes hands-on labs; its outline includes command-line operations, processes, file operations, Bash scripting, network operations, and local security.

For Week 1, concentrate on:

- Chapter 3 — Linux Basics
- Chapter 7 — Command Line Operations
- Chapter 8 — Linux Documentation
- Chapter 9 — Processes
- Chapter 10 — File Operations
- Chapter 12 — User Environment
- Chapter 13 — Manipulating Text
- Chapter 15 — Bash Shell
- Chapter 18 — Local Security


## Hands-On Tasks

* [ ] Navigate Linux filesystem
* [ ] Create/copy/move/delete files
* [ ] Understand absolute and relative paths
* [ ] Create a user
* [ ] Inspect users and groups
* [ ] Change file permissions
* [ ] Change file ownership
* [ ] Inspect running processes
* [ ] Find a process by PID
* [ ] Send SIGTERM
* [ ] Send SIGKILL
* [ ] Start/stop/restart a service
* [ ] Inspect service logs
* [ ] Write a Bash script
* [ ] Inspect CPU/memory/disk
* [ ] Troubleshoot a stopped application

## Deliverables

* `scripts/process-demo.sh`
* `scripts/system-info.sh`
* `notes/processes.md`
* `notes/permissions.md`
* `notes/signals.md`
* `troubleshooting/application-down.md`

## Final Challenge

Start a simple application, identify its process and listening port, stop it, investigate why it is unavailable, restart it, and verify recovery.

## I Can Explain

* [ ] What is a Linux process?
* [ ] What is a PID?
* [ ] What is a PPID?
* [ ] What is SIGTERM?
* [ ] What is SIGKILL?
* [ ] What is the difference between a process and a service?
* [ ] How do Linux permissions work?
* [ ] What does `chmod 755` mean?
* [ ] How do I find a process?
* [ ] How do I find a listening port?
* [ ] How do I inspect service logs?
* [ ] How do I troubleshoot a process that is not responding?

## Final Status

* [ ] Not started
* [ ] In progress
* [ ] Completed

## Biggest Lesson

Write this at the end of the week.

## Biggest Problem Solved

Write this at the end of the week.

## What I Need to Revisit

Write this at the end of the week.


## Outcome

User reports:
"My application is not responding."

You should be able to:

1. Inspect the machine
2. Find the application process
3. Identify its PID
4. Inspect CPU/memory usage
5. Inspect open ports
6. Inspect logs
7. Understand its service
8. Stop/restart it safely
9. Check permissions
10. Explain what happened