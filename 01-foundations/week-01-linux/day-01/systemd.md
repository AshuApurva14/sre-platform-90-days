# This scripts demonstrates how to manage diff services and processes using systemd commands.

# Use systemctl as your primary tool to manage services and processes on a Linux system with systemd.

systemctl --help

# It is intended to be run on a Linux system with systemd installed.

# 1. The Real time service control

# To change the state of service currently running on the system, use start, stop, restart commands with systemctl as

sudo systemctl start <service_name>
sudo systemctl stop <service_name>
sudo systemctl restart <service_name>


# 2. Boot time configuration 

# To determine whether a service should launch automatically when the computer turns on, use enable or disable:

sudo systemctl enable <service_name>

sudo systemctl disable <service_name>

# 3. Monitoring service health

# To check the status of a service, use the status command:

sudo systemctl status <service_name>
