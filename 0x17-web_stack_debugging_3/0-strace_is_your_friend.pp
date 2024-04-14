# Fix a missing file causing the 500 error
exec { 'fix-wordpress':
  command => 'touch /var/www/html/wp-settings.php',  # Create the missing file
  path    => '/usr/local/bin:/bin/',
  onlyif  => 'test ! -f /var/www/html/wp-settings.php',  # Only run if file is missing
}
