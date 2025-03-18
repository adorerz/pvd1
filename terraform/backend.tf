
terraform {
  backend "s3" {
    bucket         = "pvd-terraform-state"
    key            = "eks/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}

