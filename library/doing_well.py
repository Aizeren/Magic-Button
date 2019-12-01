from ansible.module_utils.basic import *

def main():

    fields = {
        "a": {"default": 0, "type": "int"},
        "b": {"default": 0, "type": "int"}
    }

    module = AnsibleModule(argument_spec=fields)
    a = module.params['a']
    b = module.params['b']
    res = a+b
    
    module.exit_json(changed=True, meta=res)


if __name__ == '__main__':
    main()
