# secrets

[![Build Status](https://travis-ci.org/Temelio/ansible-role-secrets.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-secrets)

Manage secrets (certificates, SSH keys, ...) deployments.

 This should be useful to remove duplicate tasks on other roles.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

### Testing dependencies
- install [Vagrant](https://www.vagrantup.com)
- install [Vagrant serverspec plugin](https://github.com/jvoorhis/vagrant-serverspec)
    $ vagrant plugin install vagrant-serverspec
- install ruby dependencies
    $ bundle install

### Running tests

#### Run playbook and test

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

## Role Variables

### Default role variables

    # CA certificates deployment
    secrets_ca_certificates_dest_folder: '/etc/ssl/certs'
    secrets_ca_certificates_dest_owner: 'root'
    secrets_ca_certificates_dest_group: 'root'
    secrets_ca_certificates_dest_mode: '0644'
    secrets_ca_certificates_from_yaml: []
    secrets_ca_certificates_from_file: []

    # Private keys deployment
    secrets_private_keys_mode: '0400'
    secrets_private_keys_from_yaml: []
    secrets_private_keys_from_file: []

## How to ...

### Manage CA certificates

Manage your vars files in your plays and simply use this syntax:

    # From YAML
    secrets_ca_certificates_from_yaml:
      - filename: 'my_ca_cert.pem'
        content: 'dqsdqsdqsdqsdqsd'
      - "{{ ca_certs.foo }}"

    # From files
    secrets_ca_certificates_from_file:
      - src: files/foo.pem
        filename: 'foo.pem'

### Manage private keys

Manage your vars files in your plays and simply use the following syntax.
If 'state' is not defined, it's same as 'present' value.

    # From YAML
    secrets_private_keys_from_yaml:
      - dest: '/home/foo/.ssh/foo.rsa'
        content: 'dqsdqsdqsdqsdqsd'
        owner: 'foo'
        group: 'foo'
      - "{{ private_keys.foo }}"

    # From files
    secrets_private_keys_from_file:
      - src: 'files/foo.pem'
        dest: '/home/foo/.ssh/foo.rsa'
        owner: 'foo'
        group: 'foo'

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: Temelio.secrets }

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://temelio.com
- alexandre.chaussier [at] temelio.com

