# autowebdriver

A tool for automatically detecting installed browsers and getting the correct web driver

Sample usage:

```python
import autowebdriver
from selenium import webdriver

browser, path = autowebdriver.getdriver() 

if browser == 'Google Chrome':
    driver = webdriver.Chrome(executable_path=path)
    
elif browser == 'Firefox':
    driver = webdriver.Firefox(executable_path=path)
    
elif browser == 'Opera':
    driver = webdriver.Opera(executable_path=path)
    
elif browser == 'Internet Explorer':
    driver = webdriver.Ie(executable_path=path)
    
elif browser == 'Edge':
    driver = webdriver.Edge(executable_path=path)

driver.get('https://google.com')
```
