resource "aws_eks_cluster" "eks_cluster" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
  }
}

resource "aws_eks_node_group" "eks_nodes" {
  cluster_name    = aws_eks_cluster.eks_cluster.name
  node_group_name = "pvd-node-group"
  node_role_arn   = aws_iam_role.eks_role.arn
  subnet_ids      = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]

  scaling_config {
    desired_size = var.eks_node_count
    max_size     = 3
    min_size     = 1
  }

  instance_types = [var.eks_instance_type]
}
