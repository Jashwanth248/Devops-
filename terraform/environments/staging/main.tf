terraform {
  required_version = ">= 1.7.0"
  required_providers { google = { source = "hashicorp/google", version = "~> 6.0" } }
}
variable "project_id" { type = string }
variable "region" { type = string default = "us-central1" }
provider "google" { project = var.project_id region = var.region }
module "network" { source = "../../modules/network" project_id = var.project_id region = var.region name = "pulsecart-staging" }
module "gke" { source = "../../modules/gke" project_id = var.project_id region = var.region name = "pulsecart-staging" network = module.network.network_id subnetwork = module.network.subnetwork_id }
