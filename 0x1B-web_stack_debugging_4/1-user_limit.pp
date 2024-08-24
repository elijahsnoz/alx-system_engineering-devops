# This puppet manifest changes the OS configuration so that it is possible to
#+ login with the holberton user and open a file without any error message.

exec { 'add soft limit for holberton user':
  command  => 'echo "holberton soft nofile 10000" >> /etc/security/limits.conf',
  unless   => 'grep -q "holberton soft nofile 10000" /etc/security/limits.conf',
  provider => shell,
}

exec { 'add hard limit for holberton user':
  command  => 'echo "holberton hard nofile 100000" >> /etc/security/limits.conf',
  unless   => 'grep -q "holberton hard nofile 100000" /etc/security/limits.conf',
  provider => shell,
}

