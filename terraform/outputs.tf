output "cluster_name" {
  value = google_container_cluster.primary.name
}

output "artifact_registry" {
  value = google_artifact_registry_repository.repo.name
}
