# Bonus: make the script fail when errors exist

Modify log-check.sh.

After the error count:

ERROR_COUNT=$(grep -c "ERROR" "$LOG_FILE")

Then:

if [ "$ERROR_COUNT" -gt 0 ]; then
    echo "ERROR: Application contains errors"
    exit 2
fi

echo "Application log is healthy"
exit 0

Now:

./scripts/log-check.sh labs/app.log
echo $?

You should get:

2

because your lab log contains errors.

This is very important for DevOps because now a script can communicate success/failure to another automation system.

That later becomes:

Bash script
   ↓
GitHub Actions
   ↓
Pipeline succeeds/fail