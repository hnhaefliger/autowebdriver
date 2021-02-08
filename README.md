# autowebdriver

A tool for automatically detecting installed browsers and getting the correct web driver

Sample usage:

```python
import autowebdriver
import selenium

browser, path = autowebdriver.getdriver() 

if browser == 'Google Chrome':
    driver = selenium.webdriver.Chrome(executable_path=path)
    
elif browser == 'Firefox':
    driver = selenium.webdriver.Firefox(executable_path=path)
    
elif browser == 'Opera':
    driver = selenium.webdriver.Opera(executable_path=path)
    
elif browser == 'Internet Explorer':
    driver = selenium.webdriver.Ie(executable_path=path)
    
elif browser == 'Edge':
    driver = selenium.webdriver.Edge(executable_path=path)
```
