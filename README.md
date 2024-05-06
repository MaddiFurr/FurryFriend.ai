# FurryFriend.ai
A fun and fluffy discord bot that I wrote to accomplish various tasks I needed or wanted on discord to save me time and effort.

This was build so that I could test different functionality and features to impliment in other areas as well.
 
# Environment Setup

1. Setup a virtual environment
py -3.12 -m venv 

2. Activate your virtual invironment in your code editor (VS Code makes this easy btw so I highly suggest using that)

(Windows)
./Scripts/Activate.ps1

(Linux)
source bin/activate

3. Install the 'requirements.txt' dependancies to ensure all the current functions of the bot work properly

# Connecting to Discord
You will need to create a 'bot.conf' file that is in an INI format. Under the "Bot" header you will need to add the TOKEN key with your Discord bot token. Beyond that, it should all just work out of the box.

# Additional Tokens
There might be additional service that exist that have been added over time that will require their own API key. You are responsible for providing it if you would like to either use or test new features with the bot using that service.

# Repo Rules
1. No contributor is permitted to push changes to master except for the owner of the Repo
2. If you would like to begin working on the bot, please create a branch and create a pull request once your feature is complete
3. The repo owner's decisions on the direction for the repo and the code are made at their descretion
