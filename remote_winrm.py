import winrm

sess = winrm.Session('https://10.10.10.10.1', auth=('Administrator', 'pass'), transport='kerberos')
result = sess.run_cmd('ipconfig', ['/all'])

