# Creates a file in /tmp

file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
