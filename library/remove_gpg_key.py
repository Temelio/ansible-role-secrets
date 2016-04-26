#!/usr/bin/python

from ansible.module_utils.basic import *  # NOQA


def main():

    module = AnsibleModule(
        argument_spec=dict(
            key_id=dict(
                type='str',
                required=True),
            key_type=dict(
                type='str',
                required=True,
                choices=['private', 'public'])
        )
    )

    # Build command to remove the key
    if (module.params['key_type'] == 'private'):
        command = "gpg --batch --yes --delete-secret-keys '%s'" % \
                  module.params['key_id']

    else:
        command = "gpg --batch --yes --delete-keys '%s'" % \
                  module.params['key_id']

    # Execute command
    rc, stdout, stderr = module.run_command(command)

    # If error occurs, fails
    if (rc != 0 and 'not found' not in stderr):
        module.fail_json(msg=stderr)

    # Manage output if no error
    has_changed = False
    if (rc == 0):
        has_changed = True

    module.exit_json(changed=has_changed, output=stdout, err=stderr)

if __name__ == '__main__':
    main()
