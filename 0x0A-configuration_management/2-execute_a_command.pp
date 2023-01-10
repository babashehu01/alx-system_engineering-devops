# Killing a process named `killmenow`

exec { 'pkill killmenow' :
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => 'shell',
}
