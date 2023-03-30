# twitter_blocklist_exporter v0.2
This is a Python3 script that uses the Twitter API to download your **Twitter blocklist** or **mutelist** and generate a HTML file with all usernames listed and clickable. You can use this list as a reference to share, mute or block unwanted accounts elsewhere.

This script was created because blocklist/mutelist exporting/importing, introduced on the platform [in 2015](https://blog.twitter.com/en_us/a/2015/sharing-block-lists-to-help-make-twitter-safer), has been absent without notice since 2019.

# Running
Just run `python3 blocklist_exporter.py`. After the script has run, your exported blocklist can be found in `blocklist.html`.
If you want to export your mutelist, add --mutelist to the command: `python3 blocklist_exporter.py --mutelist`

# Requirements
Python 3 with the [Tweepy library](https://docs.tweepy.org/en/stable/install.html) is required. Install it using `pip3 install tweepy` or through your distribution package manager.  You also need Twitter API keys. Check the section below on how to generate them.

# Sample output
```
Twitter Blocklist exporter v0.2 - https://github.com/Forceflow/twitter_blocklist_exporter
---
Loading Twitter API keys from file
Authenticating with Twitter
Grabbing blocklist
279 blocked accounts found. Writing to blocklist.html
Done. Exiting.
```
<img src="https://raw.githubusercontent.com/Forceflow/twitter_blocklist_exporter/main/sample_output.png" alt="Sample Output" width="710">

# Generate API tokens
In order to query and download your blocklist/mutelist, this script needs **API tokens** that you need to provide in a `keys.json` file in the same directory as the script.

At the time of writing (10-03-2023), this is how you generate the tokens required to export your blocklist/mutelist. Also at the time of writing, this functionality still is free for a limited amount of requests. Tweepy batches the requests as much as possible.

* Register on the **[Twitter Developer Portal](https://developer.twitter.com/)**.
* Log in, and on the [main dashboard](https://developer.twitter.com/en/portal/dashboard), go to [Projects & Apps -> overview](https://developer.twitter.com/en/portal/projects-and-apps)
* Under **Standalone Apps**, click [**Create new app**](https://developer.twitter.com/en/portal/apps/new) and give your app a unique name
* Copy the `API_KEY` and `API_KEY_SECRET`. You will only be shown these once.
* In the sidebar, select your new app, then select the **keys and tokens** tab
* At the bottom, it says **Access Token and Secret for @youraccountname**. Click **Generate**.
* Copy these values, these are `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET`
* Done! Copy `keys.json.example` to `keys.json` and fill in the `API_KEY`, `API_KEY_SECRET`, `ACESS_TOKEN` and `ACCESS_TOKEN_SECRET` values.

# Todo
* Markdown / Json export (maybe with upload integration to pastebin or elsewhere)
* Blocklist importing, if feasible
* Parsing of blocks.js from the Twitter Archive dump, for people who don't want to generate API keys
