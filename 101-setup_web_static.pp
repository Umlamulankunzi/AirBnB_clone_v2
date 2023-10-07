# Update package repository
exec { 'apt-update':
  command => 'apt update -y',
}

# Install Nginx web server
package { 'nginx':
  ensure => 'installed',
}

# Allow HTTP traffic through the firewall
exec { 'allow-http':
  command => 'ufw allow "Nginx HTTP"',
}

# Create necessary directories for web_static deployment
file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

# Create index.html file with content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
}

# Create symbolic link to latest release
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# Set ownership of the directories to 'ubuntu' user and group
exec { 'set-ownership':
  command => 'chown -R ubuntu:ubuntu /data',
}

# Configure Nginx to serve /hbnb_static/ from the current release directory
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
