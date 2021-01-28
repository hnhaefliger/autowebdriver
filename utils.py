import platform
import os
import subprocess

def getOS():
    os_name = platform.system()

    if os_name == 'Darwin':
        return 'MacOS'

    if os_name == 'Windows':
        return 'Windows'

    if os_name == 'Linux':
        return 'Linux'

def getMacOSAppVersion(program):
    version = subprocess.Popen(['mdls', '-name', 'kMDItemVersion', '/Applications/'+program+'.app'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    version = version.split('"')[1]
    return version

def findSupportedBrowsers(os_name):
    supported = ['Google Chrome', 'Firefox', 'Edge', 'Internet Explorer', 'Opera', 'Safari']
    browsers = []
    
    if os_name == 'MacOS':
        programs = os.listdir('/Applications')
        programs = [program.replace('.app', '') for program in programs if '.app' in program]
        browsers = [[program, getMacOSAppVersion(program)] for program in programs if program in supported]

    if os_name == 'Windows':
        programs = os.listdir('C:\Program Files')
        x86_programs = os.listdir('C:\Program Files (x86)')
        
        if os.path.exists('C:\Program Files\Google\Chrome'):
            version = subprocess.Popen(['wmic', 'datafile', 'where', 'name="C:\Program Files\Google\Chrome\Application\chrome"', 'get' 'Version' '/value']).communicate()[0]
            version = version.decode('utf-8')
            browsers.append(['Google Chrome', version])

        elif os.path.exists('C:\Program Files (x86)\Google\Chrome'):
            version = subprocess.Popen(['wmic', 'datafile', 'where', 'name="C:\Program Files (x86)\Google\Chrome\Application\chrome"', 'get' 'Version' '/value']).communicate()[0]
            version = version.decode('utf-8')
            browsers.append(['Google Chrome', version])

    if os_name == 'Linux':
        browsers = []
        
        try:
            chrome = subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
            chrome = chrome.decode('utf-8')
            browsers.append(chrome)

        except: pass

        try:
            firefox = subprocess.Popen(['firefox', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
            firefox = firefox.decode('utf-8')
            browsers.append(firefox)

        except: pass

    return browsers
            
print(findSupportedBrowsers(getOS()))
