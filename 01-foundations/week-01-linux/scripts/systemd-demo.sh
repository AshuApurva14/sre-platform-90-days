#!/usr/bin/env bash


# In this exercise, you will practice using systemctl to monitor and control the state of the Apache Web Server (apache2 or httpd, depending on your distribution). 
# Mastering these commands is essential for managing web services and troubleshooting connectivity issues.

# Instructions:

# 1. Check the initial status - begin by checking if the Apache service is currently active on your system.

# 2. Start the service  - if the service was inactive, or to practice the execution command, bring the server online.

# 3. Verify the change - always confirm that your command had the intended effect. Check the status again to ensure the service is now reported as active.

# 4. Stop the service - to conserve system resources or perform maintenance, shut the server down.

# 5. Final Verification - perform one last status check to ensure the service has successfully shut down.


# 1. iniitial status

sudo systemctl status apache2

# 2. Start the service

sudo systemctl start apache2

# 3. Verify the change

sudo systemctl status apache2

# 4. Stop the service

sudo systemctl stop apache2

# 5. Final Verification

sudo systemctl status apache2
