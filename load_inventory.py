from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
import json



def main():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='hosts.yml')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Print names, IP addresses, and group names of all hosts
    for host in inventory.get_hosts():
        print("Name: {}, IP: {}, Groups: {}".format(host.name, host.vars['ansible_host'], host.groups))


    passwords = {}  # Provide an empty dictionary for passwords
    

    try:
        pbex = PlaybookExecutor(playbooks=[], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
        pbex.run()
    except KeyError as e:
        # Ignore KeyError related to 'syntax'
        pass

if __name__ == '__main__':
    main()