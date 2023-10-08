terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

resource "docker_image" "nginx" {
  name = "nginxdemos/hello"
}

resource "docker_container" "nginx" {
  image = resource.docker_image.nginx.name
  name  = "nginx_hello"

  ports {
    internal  = 80
    external = 8000
  }
}