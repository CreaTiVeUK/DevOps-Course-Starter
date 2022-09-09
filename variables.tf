variable "SECRET_KEY" {
  description = ""
  sensitive   = true
}

variable "MONGO_DB_NAME" {
  description = ""
  default     = "todo"
}

variable "GITHUB_CLIENT_ID" {
  description = ""
  sensitive   = true
}

variable "GITHUB_CLIENT_SECRET" {
  description = ""
  sensitive   = true
}

variable "prefix" {
  description = "The prefix used for all resources in this environment"
}