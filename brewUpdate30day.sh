# Specify the desktop directory path for the log file
DESKTOP_DIR="/Users/erikmacbookAIR/Library/CloudStorage/Dropbox/Mac/Desktop/"

# Log file path
LOG_FILE="$DESKTOP_DIR/cron_log.txt"

#! /bin/bash
# Run the brew cleanup command and redirect output to the log file
{
    echo "---------------------"
    echo "Cron job started at: $(date)"
    
    brew update && brew upgrade
    brew cleanup
    sudo apt update && sudo apt upgrade
    brew services restart grafana-agent
    
    echo "Cron job completed at: $(date)"
} >> "$LOG_FILE" 2>&1

# Schedule the script to run every 30 days using cron
(crontab -l ; echo "0 0 */30 * * $PWD/$0 >> $LOG_FILE 2>&1") | crontab -
