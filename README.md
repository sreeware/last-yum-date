# last-yum-date
A small Python script that queries the yum sqlite database and fetch the time when the system was patched using a 'yum update|yum update -y|yum update all'. This is a quick hack and assumes that the yum database directory is /var/lib/yum/history. 
