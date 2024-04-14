# Define a resource to fix the typo in wp-settings.php
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
  # Run the command only if the file contains "phpp"
  onlyif  => '/bin/grep -q "phpp" /var/www/html/wp-settings.php',
}

# Include the class with the fix resource in your main manifest
class { 'main': }
