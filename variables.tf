variable "python_version" {
  type      = string
  default   = "3.11.2"
}

####################################################
#                python scripts vars
####################################################

variable "ansible_inventory_path" {
  type      = string
  default = "./inventory.yml"
}

variable "instance_list" {
  type      = list
  sensitive = true
}










