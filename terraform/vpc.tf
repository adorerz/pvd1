resource "aws_vpc" "pvd_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "subnet_1" {
  vpc_id                  = aws_vpc.pvd_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "subnet_2" {
  vpc_id                  = aws_vpc.pvd_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
} 

resource "aws_internet_gateway" "eks_igw" {
  vpc_id = aws_vpc.pvd_vpc.id
}

resource "aws_route_table" "eks_public_rt" {
  vpc_id = aws_vpc.pvd_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.eks_igw.id
  }
}

resource "aws_route_table_association" "subnet_1_rt" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.eks_public_rt.id
}

resource "aws_route_table_association" "subnet_2_rt" {
  subnet_id      = aws_subnet.subnet_2.id
  route_table_id = aws_route_table.eks_public_rt.id
}

