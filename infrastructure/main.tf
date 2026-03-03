terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Example: Enabling required APIs for BigQuery and Cloud Run (for the Streamlit app later)
resource "google_project_service" "apis" {
  for_each = toset([
    "bigquery.googleapis.com",
    "run.googleapis.com",
    "iam.googleapis.com"
  ])
  service            = each.key
  disable_on_destroy = false
}

# Example BigQuery Dataset for the Agent to query
resource "google_bigquery_dataset" "analytics_dataset" {
  dataset_id                  = "ai_agent_dataset"
  friendly_name               = "AI Agent Analytics Dataset"
  description                 = "Dataset for the AI Data Analyst Agent to query"
  location                    = var.region
  delete_contents_on_destroy  = true
}
