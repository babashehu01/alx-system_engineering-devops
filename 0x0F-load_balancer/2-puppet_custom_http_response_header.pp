exec { 'apt-get update':
   provider => shell,
   command  => 'sudo apt-get -y update',
}

package { 'nginx':
   ensure => installed,
   require => Exec['sudo apt-get -y update'],
}

file_line { 'header':
   ensure  => 'present',
   path    => '/etc/nginx/sites-available/default',
   after   => 'server_name _;',
   require => Package['nginx'],
   line    => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}  
