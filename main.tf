
# ------------------------------------------------------------------
# - Filename: main.tf
# - Author : draed
# - Dependency : none
# - Description : terraform module that generate ansible inventory
#  in yaml format
# - Creation date : 2025-04-30
# - terraform version : OpenTofu v1.9.0
# ------------------------------------------------------------------


# Local variables to store instance IPs and IDs
locals {
  instance_ips  = [for instance in var.instance_list : instance.ipv4]
  instance_ids  = [for instance in var.instance_list : instance.hostname]
}

resource "null_resource" "import_script_dependencies" {
  provisioner "local-exec" {
    command = "virtualenv -p ${var.python_version} ${path.module}/venv && ${path.module}/venv/bin/python -m pip install -r ${path.module}/scripts/requirements.txt"
  }
}

resource "null_resource" "generate_ansible_inventory" {
  depends_on = [null_resource.import_script_dependencies]
  provisioner "local-exec" {
    command = "${path.module}/venv/bin/python ${path.module}/scripts/generate_ansible_inventory.py"
    environment = {
      INSTANCE_IPS = "${join(",", local.instance_ips)}"
      INSTANCE_IDS = "${join(",", local.instance_ids)}"
      ANSIBLE_INVENTORY_PATH = var.ansible_inventory_path
    }
  }
}

