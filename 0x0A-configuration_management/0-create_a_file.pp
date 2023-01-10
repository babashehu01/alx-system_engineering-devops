# Creates a file in /tmp

file { '/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
