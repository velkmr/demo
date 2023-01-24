terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.51.0"
    }
  }
}

provider "aws" {
    #access_key = var.access
    #secret_key = var.secret 
    #region  = var.region
}



resource "aws_iam_policy" "policy" {
  name        = var.policy_name
  path        = "/"
  description = "My test policy"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
variable "policy_name"{
type = string

}