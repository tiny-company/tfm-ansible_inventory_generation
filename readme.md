# tfm-ansible_inventory_generation

## Description

A simple terraform module that generate an ansible inventory in yaml format from terraform.

## Usage

- Import the module by referencing it in your main terraform file (`main.tf`) using :
```hcl
module "pfsense_register_static_dhcp_mapping" {
  source     = "git::https://github.com/tiny-company/tfm-ansible_inventory_generation.git"
  ansible_inventory_path = var.ansible_inventory_path
  instance_list = var.instance_list
}
```

- Don't forget to define the vars below in your main variables.tf :
```hcl
variable "python_version" {
  type      = string
  default   = "3.11.2"
}

variable "ansible_inventory_path" {
  type      = string
  default = "./inventory.yml"
}

variable "instance_list" {
  type      = list
  sensitive = true
}

```

- And finally don't forget to set **these vars** and **the vars for the proxmox/bpg provider** in a .tfvars (i.e: `terraform.tfvars`) file  :
```hcl
ansible_inventory_path="./inventory.yml"
instance_list=[{"ipv4": "192.168.1.1", "hostname": "test1"},{"ipv4": "192.168.1.2", "hostname": "test2"}]
```

## Sources :

- [tutorial terraform module](https://developer.hashicorp.com/terraform/tutorials/modules/module)
- [terraform module creation guide](https://developer.hashicorp.com/terraform/language/modules/develop)
- [terraform module source](https://developer.hashicorp.com/terraform/language/modules/sources#github)
- [terraform module git private repo source](https://medium.com/@dipandergoyal/terraform-using-private-git-repo-as-module-source-d20d8cec7c5)