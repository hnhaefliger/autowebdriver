import os
import subprocess

def getAppVersion(app):
    '''
    Get the version of an app that is installed on macos
    '''
    version = subprocess.Popen(['mdls', '-name', 'kMDItemVersion', app], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    version = version.split('"')[1]
    return version

def findBrowsers():
    '''
    List browsers and versions installed on a macos operating system

    Safari gets last priority because it needs to be set up for selenium by
    developers rather than with a driver.
    '''
    supported = ['Google Chrome', 'Firefox', 'Opera', 'Safari']
    
    global_apps = os.listdir('/Applications')
    global_apps = [app.replace('.app', '') for app in global_apps if '.app' in app]
    global_apps = [[app, getAppVersion('/Applications/' + app + '.app'), 64] for app in global_apps if app in supported]

    user_apps = os.listdir(os.path.expanduser('~/Applications')) # Preference for non user-specific applications
    user_apps = [app.replace('.app', '') for app in user_apps if '.app' in app]
    user_apps = [[app, getAppVersion(os.path.expanduser('~/Applications/') + app + '.app'), 64] for app in user_apps if app in supported]
    user_apps = [app for app in user_apps if not(app in global_apps)]

    browsers = global_apps + user_apps

    return browsers
