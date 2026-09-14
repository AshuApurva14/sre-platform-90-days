# inal recovery lab

Now pretend you're on call.

You receive:

"The application's log has errors."

Run:

./scripts/log-check.sh labs/app.log

Your script should tell you:

Total lines
ERROR count
WARN count
Actual errors
Actual warnings

Now ask yourself:

Could I run this every 5 minutes?

Could I make it return an error code when ERROR count > 0?

That last question is where we'll eventually move toward monitoring and CI/CD.