import platform
import os
import subprocess

def getAppVersion(app):
    version = subprocess.Popen([app, '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    return version

def findBrowsers():
    supported = ['Google Chrome', 'Firefox', 'Edge', 'Internet Explorer', 'Opera', 'Safari']
    browsers = []

    try:
        subprocess.Popen(['google-chrome'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Google Chrome', getAppVersion('google-chrome')])

    except: pass

    try:
        subprocess.Popen(['firefox'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Firefox', getAppVersion('firefox')])

    except: pass

    try:
        subprocess.Popen(['opera'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Opera', getAppVersion('opera')])

    except: pass

    return browsers
