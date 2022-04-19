#Using Puppet, install puppet-lint 2.5.0.

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem',
    name     => 'puppet-lint',
    source   => 'https://rubygems.org/downloads/',
}
