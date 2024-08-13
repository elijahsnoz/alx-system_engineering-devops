# This Puppet manifest fixes a typo in the file name by renaming it.
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test -f /var/www/html/wp-includes/class-wp-locale.phpp',
}
