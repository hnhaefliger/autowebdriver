import autowebdriver

print(getDriverURL('Google Chrome', '86.0.4240.111', 'Darwin', '64'))
print(getDriverURL('Opera', '72.0', 'Darwin', '64'))
print(getDriverURL('Edge', '75.0.139.20', 'Windows', '64'))
print(getDriverURL('Internet Explorer', '75.0.139.20', 'Windows', '64'))
print(getDriverURL('Firefox', '75.0.139.20', 'Darwin', '64'))

print(autowebdriver.getdriver())
