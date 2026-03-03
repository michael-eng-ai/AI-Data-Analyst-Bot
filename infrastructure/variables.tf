variable "project_id" {
  description = "The ID of the Google Cloud Project"
  type        = string
  default     = "seu-projeto-gcp-id"
}

variable "region" {
  description = "The region for GCP resources"
  type        = string
  default     = "us-central1"
}
