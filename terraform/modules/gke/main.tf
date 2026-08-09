variable "project_id" { type = string }
variable "region" { type = string }
variable "name" { type = string }
variable "network" { type = string }
variable "subnetwork" { type = string }

resource "google_container_cluster" "this" {
  project  = var.project_id
  name     = var.name
  location = var.region
  network    = var.network
  subnetwork = var.subnetwork
  remove_default_node_pool = true
  initial_node_count       = 1
  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }
  release_channel { channel = "REGULAR" }
  ip_allocation_policy {}
}

resource "google_container_node_pool" "general" {
  project    = var.project_id
  name       = "general"
  cluster    = google_container_cluster.this.name
  location   = var.region
  node_count = 2
  autoscaling { min_node_count = 2 max_node_count = 6 }
  node_config {
    machine_type = "e2-standard-4"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
