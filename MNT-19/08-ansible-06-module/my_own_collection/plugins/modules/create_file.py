#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file

short_description: This is my module for netology

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This module creates the file in a specific path with specific content.

options:
    path:
        description: path where module will create the file.
        required: true
        type: str
    content:
        description: content of the file
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - netology.study.create_file

author:
    - Tokhir Abidov
'''

EXAMPLES = r'''
# create file in path "/test_directory/file1" with content "hello world"
- name: Test with a message
  netology.study.create_file:
    path: /test_directory/file1
    content: hello world
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: message about the success of creating the file
    type: str
    returned: always
    sample: 'File /test_directory/file1 was created and filled with your content'
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message='Nothing is done'
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    path = module.params['path']
    content = module.params['content']

    if os.path.isfile(path):
        fileContent = open(path, "r").read()
        if fileContent == content:
            result['changed'] = False
            result['message'] = "File is already up to date"
            module.exit_json(**result)
    
    errorMessage = ""
    try:
        file = open(path, "w")
        file.writelines(content)
    except Exception as e:
        errorMessage = str(e)
        result['changed'] = False
        result['message'] = "Something's gone wrong"
    else:
        result['changed'] = True
        result['message'] = "File " + path + " was created and filled with your content"
    
    if len(errorMessage) > 0:
        module.fail_json(msg=errorMessage, **result)
    else:
        file.close
        module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
