#Using Puppet, create a file in /tmp.

file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    mode    => '0744',
    group   => 'www-data',
    path    => '/tmp/school',
    content => 'I love Puppet',
}
