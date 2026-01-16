#!/bin/bash

# Default to every hour if not set
CRON_SCHEDULE="${CRON_SCHEDULE:-0 * * * *}"

echo "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" > /etc/cron.d/elt-cron
echo "$CRON_SCHEDULE python3 /app/elt_pipeline.py >> /proc/1/fd/1 2>&1" >> /etc/cron.d/elt-cron

# Write out the cron job
#echo "$CRON_SCHEDULE python3 /app/elt_pipeline.py >> /proc/1/fd/1 2>&1" > /etc/cron.d/elt-cron

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/elt-cron

# Apply cron job
crontab /etc/cron.d/elt-cron

# Start cron in foreground
cron -f
