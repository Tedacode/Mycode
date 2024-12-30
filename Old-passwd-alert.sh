#!/bin/bash

# Adminstrator email
ADMIN_EMAIL="admin@mail.com"

# Number of days before sending notification 
THRESHOLD_DAYS=90 

# Temporary file for email content 
EMAIL_BODY="/tmp/password_update_email.txt" 

# Clear the email body file 
> "$EMAIL_BODY" 

# Header for the email body 
echo "Subject: Password Update Alert" > "$EMAIL_BODY" 
echo "The following users have not updated their passwords in the last $THRESHOLD_DAYS days:" >> "$EMAIL_BODY" 
echo >> "$EMAIL_BODY" 

# Flag to determine if we should send the email 
SEND_EMAIL=false 

# Loop through all users 
while IFS=: read -r username _ _ uid _ _ _; do 
    # Skip system accounts 
    if [ "$uid" -lt 1000 ] && [ "$uid" -ne 0 ]; then 
        continue 
    fi 
    
    # Get the last password change date in days 
    last_change=$(chage -l "$username" | grep "Last password change" | awk -F': ' '{print $2}')

    # Skip users with no recorded password change 
    if [[ "$last_change" == "never" ]]; then 
        continue 
    fi

    # Convert last_change to days since epoch 
    last_change_days=$(date -d "$last_change" +%s) 
    current_days=$(date +%s) 
    days_diff=$(( (current_days - last_change_days) / 86400 )) 

    # Check if the difference exceeds the threshold 
    if [ "$days_diff" -ge "$THRESHOLD_DAYS" ]; then 
        SEND_EMAIL=true     
        echo "- $username (last changed $days_diff days ago)" >> "$EMAIL_BODY" 
    fi 
done < /etc/passwd

# Check if we need to send the email 
if $SEND_EMAIL; then 
    # Send the email
    /usr/sbin/sendmail -t < "$EMAIL_BODY" 
fi 

# Clean up
rm -f "$EMAIL_BODY"
