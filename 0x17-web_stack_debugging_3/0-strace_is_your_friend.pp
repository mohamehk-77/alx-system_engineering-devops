# Fix a missing file causing the 500 error
exec { 'fix-wordpress':
  command => 'touch /var/www/html/wp-settings.php',  # Create the missing file
  path    => '/usr/local/bin:/bin/',
  onlyif  => 'test ! -f /var/www/html/wp-settings.php',  # Only run if file is missing
}

# Ensure Apache user has read access to wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure => present,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}
