provider "aws" {
  region = "us-east-2"
  profile = "op-terraform"
  access_key = "AKIAU4FALUDERILN7OUC"
  secret_key = "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"
}

resource "aws_instance" "desafio-dock"{
  ami = "ami-0603cbe34fd08cb81"
  instance_type = "t2.micro"


	metadata_options {
	    http_endpoint               = "enabled"
	    http_tokens                 = "required"
	    http_put_response_hop_limit = 1
	}
}
