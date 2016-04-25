#!/usr/bin/python


from ansible.module_utils.basic import *  # NOQA
import random


# Check keyservers param contains only non empty string
def is_valid_key_servers_list(key_servers):
    """
    Check if key servers list contains only not empty strings

    :param key_servers: Key servers list
    :type key_servers: list
    :return: True if key servers list is valid, False otherwise
    :rtype: Boolean
    """

    for entry in key_servers:
        if (type(entry) != str or len(entry) == 0):
            return False

    return True


def main():

    module = AnsibleModule(
        argument_spec=dict(
            import_type=dict(
                type='str',
                required=True,
                choices=['file', 'keyserver']),
            key_path=dict(
                type='str',
                required=False),
            key_id=dict(
                type='str',
                required=False),
            key_servers=dict(
                type='list',
                required=False)
        )
    )

    # Build command to import the key
    if (module.params['import_type'] == 'file'):
        command = "gpg --batch --yes --import '%s'" % \
                  module.params['key_path']

    else:
        if (is_valid_key_servers_list(module.params['key_servers']) is False):
            error_msg = "Keyservers param must contains only non empty strings"
            module.fail_json(msg=error_msg)

        # Pick a random keyserver from list
        keyserver = random.choice(module.params['key_servers'])

        command = "gpg --batch --yes --keyserver '%s' --recv-keys '%s'" % \
            (keyserver, module.params['key_id'])

    # Execute command
    rc, stdout, stderr = module.run_command(command)

    # If error occurs, fails
    if (rc != 0):
        module.fail_json(msg=stderr)

    # Manage output if no error
    has_changed = False
    if ('imported: 1' in stderr):
        has_changed = True

    module.exit_json(changed=has_changed, output=stdout, err=stderr)

if __name__ == '__main__':
    main()
