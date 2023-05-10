# twitternamewatch
Quick script to monitor username availability on Twitter. For the homies.

Requires Twitter API access (only got charged $80 for the $100 tier 💸)

___

Use: Fill in placeholders in both files, run nameCheck.py
___

Limited to one call every ~173 seconds 
  based on API tier limit of 500 app requests per 24 hrs... 
   feel free to turbo if you're feelin lucky

Plays an annoying beep for 5 seconds and exits when the request JSON includes "error" (otherwise returns "data" if account still exists)

Updated to include and call selenium script - webdrive Google Voice and text me that the time is nigh.
