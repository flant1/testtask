terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.17.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

variable "servicename" {
  type        = string
}
variable "imagename" {
  type        = string
}

resource "docker_service" "foo" {
  name = var.servicename

  task_spec {
    container_spec {
      image = var.imagename
    }
  }

  mode {
    global = true
  }

  endpoint_spec {
    ports {
      target_port = "8080"
      published_port = "8080"
    }
  }
}
