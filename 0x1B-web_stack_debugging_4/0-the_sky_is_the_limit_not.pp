# Fix failed request 0
exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}
exec { 'service nginx restart':
  command => '/usr/sbin/service nginx restart'
}