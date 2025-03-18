variable "aws_region" {
  default = "us-east-1"
}

variable "cluster_name" {
  default = "pvd-cluster"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "eks_instance_type" {
  default = "t3.medium"
}

variable "eks_node_count" {
  default = 2
}
