# 100-puppet_ssh_config.pp
file { '/home/vagrant/.ssh/config':
  ensure  => 'file',
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  content => template('ssh/config.erb'),
}

file_line { 'Declare identity file':
  path  => '/home/vagrant/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

file_line { 'Turn off passwd auth':
  path  => '/home/vagrant/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}

