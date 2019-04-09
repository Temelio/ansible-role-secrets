# secrets

[![Build Status](https://travis-ci.org/Temelio/ansible-role-secrets.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-secrets)

Install secrets package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# CA certificates deployment
secrets_ca_certificates_dest_folder: '/etc/ssl/certs'
secrets_ca_certificates_dest_owner: 'root'
secrets_ca_certificates_dest_group: 'root'
secrets_ca_certificates_dest_mode: '0644'
secrets_ca_certificates_from_yaml: []
secrets_ca_certificates_from_file: []

# Private SSL files deployment
secrets_private_ssl_dest_folder: '/etc/ssl/private'
secrets_private_ssl_dest_owner: 'root'
secrets_private_ssl_dest_group: 'root'
secrets_private_ssl_dest_mode: '0400'
secrets_private_ssl_from_yaml: []
secrets_private_ssl_from_file: []

# SSH private keys deployment
secrets_ssh_private_keys_mode: '0400'
secrets_ssh_private_keys_from_yaml: []
secrets_ssh_private_keys_from_file: []

# GPG public keys management
secrets_gpg_public_keys_from_yaml: []
secrets_gpg_public_keys_from_file: []
secrets_gpg_public_keys_from_keyserver: []
secrets_gpg_public_keys_to_remove: []
secrets_gpg_import_keyserver_retries: 5
secrets_gpg_import_keyserver_delay: 10
secrets_gpg_key_servers:
  - 'keys.gnupg.net'
  - 'hkp://subkeys.pgp.net'
  - 'pgp.mit.edu'
  - 'pool.sks-keyservers.net'
  - 'keyserver.ubuntu.com'
```

## How to ...

### Manage CA certificates

Manage your vars files in your plays and simply use this syntax:

``` yaml
# From YAML
secrets_ca_certificates_from_yaml:
  - filename: 'my_ca_cert.pem'
    content: 'dqsdqsdqsdqsdqsd'
  - "{{ ca_certs.foo }}"
# From files
secrets_ca_certificates_from_file:
  - src: files/foo.pem
    filename: 'foo.pem'
```

### Manage SSH private keys

Manage your vars files in your plays and simply use the following syntax.
If 'state' is not defined, it's same as 'present' value.

``` yaml
# From YAML
secrets_ssh_private_keys_from_yaml:
  - dest: '/home/foo/.ssh/foo.rsa'
    content: 'dqsdqsdqsdqsdqsd'
    owner: 'foo'
    group: 'foo'
  - "{{ private_keys.foo }}"
# From files
secrets_ssh_private_keys_from_file:
  - src: 'files/foo.pem'
    dest: '/home/foo/.ssh/foo.rsa'
    owner: 'foo'
    group: 'foo'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.secrets }
```

## License

MIT

## Author Information

A. Chaussier, L. Machetel (for Temelio company)
- https://www.temelio.com
