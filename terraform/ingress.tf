resource "aws_lb" "eks_lb" {
  name               = "pvd-loadbalancer"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.eks_sg.id]
  subnets           = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
}
