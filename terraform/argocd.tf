
resource "null_resource" "install_argocd" {
  depends_on = [aws_eks_cluster.eks_cluster]

  provisioner "local-exec" {
    command = <<EOT
      echo "Waiting for EKS to be ready..."
      sleep 60  # Add delay to ensure EKS is ready
      aws eks update-kubeconfig --region us-east-1 --name pvd-cluster
      kubectl create namespace argocd
      kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    EOT
  }
}

