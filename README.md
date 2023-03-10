# twitter_blocklist_exporter v0.1
This is a Python3 script that uses the Twitter API to download your most recent blocklist and generate a HTML file with all usernames listed and clickable. 

# Running
Just run `python3 blocklist_exporter.py`. After the script has run, your exported blocklist can be found in `blocklist.html`.

# Requirements
Python 3 with the [Tweepy library](https://docs.tweepy.org/en/stable/install.html) is required. Install it using `pip3 install tweepy` or through your distribution package manager.  You also need Twitter API keys. Check the section below on how to generate them.

# Sample output
```
Twitter Blocklist exporter v0.1 - https://github.com/Forceflow/twitter_blocklist_exporter
---
Loading Twitter API keys from file
Authenticating with Twitter
Grabbing blocklist
279 blocked accounts found. Writing to blocklist.html
Done. Exiting.
```
<img src="https://raw.githubusercontent.com/Forceflow/twitter_blocklist_exporter/main/sample_output.png" alt="Sample Output" width="710">

# Generate API tokens
In order to query and download your blocklist, this script needs **API tokens** that you need to provide in a `keys.json` file in the same directory as the script.

At the time of writing (10-03-2023), this is how you generate the tokens required to export your blocklist.

* Register at the **[Twitter Developer Portal](https://developer.twitter.com/)**
* Log in, and on the [main dashboard](https://developer.twitter.com/en/portal/dashboard), go to [Projects & Apps -> overview](https://developer.twitter.com/en/portal/projects-and-apps)
* Under **Standalone Apps**, click [**Create new app**](https://developer.twitter.com/en/portal/apps/new) and give your app a unique name
* Copy the `API_KEY` and `API_KEY_SECRET`. You will only be shown these once.
* In the sidebar, select your new app, then select the **keys and tokens** tab
* At the bottom, it says **Access Token and Secret for @youraccountname**. Click **Generate**.
* Copy these values, these are `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET`
* Done! Copy `keys.json.example` to `keys.json` and fill in the `API_KEY`, `API_KEY_SECRET`, `ACESS_TOKEN` and `ACCESS_TOKEN_SECRET` values.
