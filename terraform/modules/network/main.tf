variable "project_id" { type = string }
variable "region" { type = string }
variable "name" { type = string }

resource "google_compute_network" "this" {
  project                 = var.project_id
  name                    = var.name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "gke" {
  project       = var.project_id
  name          = "${var.name}-gke"
  region        = var.region
  network       = google_compute_network.this.id
  ip_cidr_range = "10.20.0.0/20"
  secondary_ip_range {
    range_name    = "pods"
    ip_cidr_range = "10.24.0.0/14"
  }
  secondary_ip_range {
    range_name    = "services"
    ip_cidr_range = "10.28.0.0/20"
  }
}

output "network_id" { value = google_compute_network.this.id }
output "subnetwork_id" { value = google_compute_subnetwork.gke.id }
