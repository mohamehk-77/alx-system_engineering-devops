# Ensure Apache user has read access to wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure => present,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}
