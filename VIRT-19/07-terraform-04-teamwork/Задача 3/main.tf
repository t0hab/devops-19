provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id                 = "b1g9ihitksj8pk4q71d5"
  folder_id                = "b1giimrttnp35tj922g5"
  zone                     = "ru-central1-a"
}

data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2004-lts"
}

resource "yandex_vpc_network" "net" {
  name = "net"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "subnet"
  network_id     = resource.yandex_vpc_network.net.id
  v4_cidr_blocks = ["10.2.0.0/16"]
  zone           = "ru-central1-a"
}

module "compute" {
 source = "t0hab/compute/yandex"
 version = "0.1.2"

 image_family = "ubuntu-2004-lts"
 subnet = "subnet"
 folder_id = "b1gfege9gjopte1c9qa1"

 name = "ec2_netology"
 hostname = "dev"
 is_nat = true

 cores = local.cores[terraform.workspace]
 memory = local.memory[terraform.workspace]
 size = local.size[terraform.workspace]

}

locals {
  web_instance_count_map = {
    stage = 1
    prod = 2
  }
  cores ={
    stage = 2
    prod = 4
  }
  memory = {
    stage = 2
    prod = 4
  }
  size = {
    stage = 10
    prod = 20
  }
}