terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "StandardChartered21_SimeonPenev_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-todo-app-simeon"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image     = "simeonp901/todo_app"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "MONGO_CON_STRING"           = azurerm_cosmosdb_account.main.connection_strings[0]
    "MONGO_DB_NAME"              = var.MONGO_DB_NAME
    "GITHUB_CLIENT_ID"           = var.GITHUB_CLIENT_ID
    "GITHUB_CLIENT_SECRET"       = var.GITHUB_CLIENT_SECRET
    "SECRET_KEY"                 = var.SECRET_KEY
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-cosmos-db-creativeuk"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  lifecycle {
    prevent_destroy = true
  }

  geo_location {
    location          = data.azurerm_resource_group.main.location
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}-cosmos-mongo-db"
  resource_group_name = azurerm_cosmosdb_account.main.resource_group_name
  account_name        = azurerm_cosmosdb_account.main.name
}

