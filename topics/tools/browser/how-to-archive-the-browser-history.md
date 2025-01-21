# How to archive the browser history

### On Firefox (linux)

Find the `places.sqlite` file as described [here](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data#w_finding-your-profile-without-opening-firefox):

Go to `~/.mozilla/firefox`

Navigate in the folder which has "default" in its name.

This folder contains the `places.sqlite` file.

Copy it to your backup folder.

The data in the file can be decoded in the [following](read-the-places-sqlite-file.md) way.