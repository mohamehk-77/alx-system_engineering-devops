# fix apachi server to run properly run wordpress site 

exec { 'fix_wp_settings':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/local/bin/', '/bin/'],
}
