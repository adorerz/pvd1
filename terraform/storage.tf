resource "aws_ebs_volume" "k8s_storage" {
  availability_zone = "us-east-1a"
  size              = 50
}
