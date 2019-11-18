#!/usr/bin/python

# python wrapper for dockutil. We use the --no-restart flag for most of this
# to reduce the amount of flashes (to one) that occur on the user's desktop.

# Written by Erik Gomez
# Edited by Andrew Doering - 2019/05/16
# Updated on 2019/09/20 - Add Mojave and Catalina support check - basically an if statement

import os
import subprocess
import platform


def dockutil(type, itempath, norestart):
    if norestart is True:
        cmd = ['/usr/local/bin/dockutil', type, itempath, '--no-restart']
    else:
        cmd = ['/usr/local/bin/dockutil', type, itempath]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return output
    except Exception:
        return None


def dockutilFolder(type, itempath, norestart, sorttype):
    if norestart is True:
        cmd = ['/usr/local/bin/dockutil', type, itempath, '--sort', sorttype,
               '--no-restart']
    else:
        cmd = ['/usr/local/bin/dockutil', type, itempath, '--sort', sorttype]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return output
    except Exception:
        return None


def main():
    # Remove all dock items.
    dockutil('--remove', 'all', True)

    # Add the paths of the items you want to add to the dock here.
    applistCatalina = [
        '/System/Applications/Launchpad.app',
        '/Applications/Google Chrome.app',
        '/Applications/Google Mail.app',
        '/Applications/Google Contacts.app',
        '/Applications/Google Calendar.app',
        '/Applications/Google Drive.app',
        '/Applications/Google Docs.app',
        '/Applications/Google Sheets.app',
        '/Applications/Google Slides.app',
        '/Applications/Slack.app',
        '/Applications/zoom.us.app',
        '/Applications/Managed Software Center.app',
        '/System/Applications/System Preferences.app',
    ]
    applistMojave = [
        '/Applications/Launchpad.app',
        '/Applications/Google Chrome.app',
        '/Applications/Google Mail.app',
        '/Applications/Google Contacts.app',
        '/Applications/Google Calendar.app',
        '/Applications/Google Drive.app',
        '/Applications/Google Docs.app',
        '/Applications/Google Sheets.app',
        '/Applications/Google Slides.app',
        '/Applications/Slack.app',
        '/Applications/zoom.us.app',
        '/Applications/Managed Software Center.app',
        '/Applications/System Preferences.app',
    ]


    v = platform.mac_ver()[0]
    v = float('.'.join(v.split('.')[:2]))
    if v >= 10.15:
        for itempath in applistCatalina:
            if os.path.isdir(itempath):
                dockutil('--add', itempath, True)
    else:
        for itempath in applistMojave:
            if os.path.isdir(itempath):
                dockutil('--add', itempath, True)

    # Tell dockutil to restart and finally update the dock.
    dockutilFolder('--add', '~/Downloads', False, 'name')


if __name__ == '__main__':
    main()
