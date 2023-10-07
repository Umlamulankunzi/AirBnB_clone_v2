# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories for web_static deployment
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

-> file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

-> file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

-> file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create index.html file with content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Hello, world!\n  </body>\n</html>\n',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link to the latest release
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration to serve /hbnb_static/ from the current release directory
file_line { 'nginx-config':
  path    => '/etc/nginx/sites-available/default',
  line    => '  location /hbnb_static/ { alias /data/web_static/current/; }',
  match   => 'listen 80 default_server',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx to apply the configuration changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}


# Exit with a successful status
exec { 'exit-success':
  command => 'exit 0',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test $? -ne 0',
}
