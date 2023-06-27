# localstack101
## Installation (Ubuntu-22.04)
- Docker
  - [Docker](https://docs.docker.com/engine/install/ubuntu/)
- Terraform
  - **sudo snap install terraform —classic**
## Commands
- Docker
  - First run the docker container via this command
      - **sudo docker run --rm -it -p 4566:4566 -p 4571:4571 -v /var/run/docker.sock:/var/run/docker.sock localstack/localstack**
  - This command will try to find already installed localstack. If not found it will automatically install localstack on machine.
- Terraform
  - **terraform init**, this command will look for dependency and intall it if already not installed.
  - **terraform plan**, this command will stage and plan for any cloud deployment. We can check if everything is right to deploy.
  - **terraform apply** this command will apply the planned deployment. Terraform is a layer before deployment. To learn more visit [Terraform website](https://www.terraform.io/)
## main.tf
- In this file currently I applied the endpoints of aws services to localstack.
- Then created a aws iam role.
- Applied required resources for api gateway.
- Created a lambda function that prints a json data after invoking the url
    - http://localhost:4566/restapis/<API_GW_ID>/test/_user_request_/my_api_route
