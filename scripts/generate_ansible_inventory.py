# ------------------------------------------------------------------
# - Filename: generate_ansible_inventory.py
# - Author : draed
# - Dependency : none
# - Description : python script that generate ansible inventory
#   in yaml format from terraform output
# - Creation date : 2025-05-02
# - Python version : 3.11.2
# ------------------------------------------------------------------

import os
import yaml
from dotenv import load_dotenv

def generate_ansible_inventory(ansible_inventory_path: str, instance_ips: list, instance_ids: list):
    """

    Parameters:
    - ansible_inventory_path : the ansisble inventory file path to generate to
    - instance_ips : list of instance ips
    - instance_ids : list of instancd ids (hostname)

    Returns:
    - nothing

    Raises:
    - ValueError: If an error occured while generating yaml inventory file
    """

    try:
        inventory = {
            'all': {
                'hosts': {}
            }
        }

        for instance_id, instance_ip in zip(instance_ids, instance_ips):
            inventory['all']['hosts'][instance_id] = {
                'ansible_host': instance_ip
            }

        with open(ansible_inventory_path, 'w') as f:
            yaml.dump(inventory, f, default_flow_style=False)

        print(f"Successfully generate ansible inventory at path : {ansible_inventory_path}")

    except Exception as e:
        raise ValueError(f'An error occurred: {e}')
        return None


if __name__ == "__main__":
    instance_ips = os.getenv('INSTANCE_IPS', '').split(',')
    instance_ids = os.getenv('INSTANCE_IDS', '').split(',')
    ansible_inventory_path = os.getenv('ANSIBLE_INVENTORY_PATH', '')
    generate_ansible_inventory(ansible_inventory_path, instance_ips, instance_ids)

