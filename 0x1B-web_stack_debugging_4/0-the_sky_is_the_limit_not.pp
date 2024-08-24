# This Puppet manifest configures Nginx to handle a higher load by adjusting worker processes and connections

exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections 768;/worker_connections 4096;/" /etc/nginx/nginx.conf && service nginx restart',
}

