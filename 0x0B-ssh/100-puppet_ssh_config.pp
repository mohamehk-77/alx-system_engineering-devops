#!usr/bin/env bash
#use puppet to make changes to my config files
#this script is to be run on the puppet master
file { '/etc/ssh/ssh_config':
        ensure => present,
content => "
Include /etc/ssh/ssh_config.d/*.conf
Host *
    IdentityFile ~/.ssh/school
    passwordAuthentication no
",
  mode    => '0644',
}
