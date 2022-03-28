terraform {
  backend "s3" {
    bucket         = "reggie-talent-academy-686520628199-tfstates"
    key            = "sprint2/week2/training-terraform-ec2/terraform.tfstates"
    dynamodb_table = "terraform-lock"
  }
}