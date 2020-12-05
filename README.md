**Index**


[TOC]
## Introduction
In this repository, it will be explained how simple Docker in **AWS Amazon Elastic Container Service (ECS)** with **AWS Fargate** can be created using his **AWS API** and **Python3**.
**Amazon Fargate** is a serverless container execution solution offered to customers who dont want to choose server types, scale clusters, or optimize them. https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html

**More information**
- Region used: **us-east-1**
- **AWS API CLI V2**
- **Python3** and **boto3**  (Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python3).

I have wanted to explain it the easiest way using steps and images. I hope you find it useful.

##Create new API User to get tokens
Using this link https://console.aws.amazon.com/iam/home?region=us-east-1#/users will be created our API user that be used after.
- Step 1
> ![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/NewUserAPi.png)

- Step 2
> ![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/NewUserAPi2.png)

- Step 3
Important: Add all ECS Polices and AmazonEC2ContainerRegistryFullAccess
> ![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/NewUserAPi3.png)
> ![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/NewUserAPi3-2.png)

- Step 4
Finally: Save the Access Key ID and Secret Access Key
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/NewUserAPi4.png)

##Creating IAM Perms and Roles
- Step 1
In the same page will be selected Roles
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/CreateRoles.png)

- Step 2
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/CreateRoles2.png)

- Step 3
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/CreateRoles3.png)

- Step 4
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/CreateRoles4.png)

- Step 5
Important: The name role must be called ECSTaskExecutionRole
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/CreateRoles5.png)

##Install AWS CLI version 2
Using this link https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html you may install AWS CLI version 2.
After that you can use the command `aws configure` and follow the steps

>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/awscli.png)

Great, ready to using the AWS CLI with you API User credentials
##Push simple Docker with Flask API to ECR Service
In the repository it will had a folder with a simple Docker with Flask API library. The Flask up the service into port 80 and it return a simple "OK".
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/docker.png)

Using this link https://us-east-1.console.aws.amazon.com/ecr/repositories?region=us-east-1 going to ECR service page
- Step 1
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR.png)

- Step 2
For this example it will be leaved all the default values, just add the Repository name
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR2.png)

- Step 3
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR3.png)
- Step 4
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR3-1.png)

- Step 5
Execute this commands one by one from Docker repository folder
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR3-2.png)

- Step 6
If everything works fine we will have our Docker into AWS ECR service
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR3-4.png)

- Step 7
Don't forget copy and save the Image URI, example: **XXXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/image-demo:latest**
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECR4.png)

If you want you can optimizate the **RAM** or **CPU** you can change it in the code:

>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/code2.png)

**Supported task CPU and memory values for Fargate tasks are as follows:**

| CPU value |	Memory value (MiB) |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 256 (.25 vCPU) |	512 (0.5GB), 1024 (1GB), 2048 (2GB)                                                                              |
| 512 (.5 vCPU)	  | 1024 (1GB), 2048 (2GB), 3072 (3GB), 4096 (4GB)                                                             |
| 1024 (1 vCPU)	 | 2048 (2GB), 3072 (3GB), 4096 (4GB), 5120 (5GB), 6144 (6GB), 7168 (7GB), 8192 (8GB)   |
| 2048 (2 vCPU)	 | Between 4096 (4GB) and 16384 (16GB) in increments of 1024 (1GB)                               |
| 4096 (4 vCPU)	 | Between 8192 (8GB) and 30720 (30GB) in increments of 1024 (1GB)                               |

*Show the pricing https://aws.amazon.com/fargate/pricing/?nc1=h_ls

##Code customization
You must change the parametres values with yours `accessKey`, `secretKey` and `image` as well as `subnets` and `securityGroups` for you VPC, for this example works any that you had created.
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/code1.png)

##Running tests
- Step 1
Run the `pip3 install -r requirements.txt` to install boto3.

- Step 2
Run the `ecs.py` file with Python3
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/code3.png)

- Step 3
Using this link https://us-east-1.console.aws.amazon.com/ecs/home?region=us-east-1#/clusters to go your cluster and the get Task information
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECS.png)

- Step 4
The task information shows us the Docker public IP
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/ECS2.png)

- Step 5
Go to this IP in your browser to check if the Docker is running well
>![](https://raw.githubusercontent.com/Neorichi/ECSFargateBoto3/main/images/dockerunwell.png)

#About
## Author

**Ricardo Sánchez**

* [github/neorichi](https://github.com/neorichi)
* [twitter/neorichi](http://twitter.com/neorichi)

## License

Copyright &copy; 2020, [Ricardo Sánchez](https://github.com/neorichi).
Released under the [MIT license](https://github.com/generate/generate-readme/blob/master/LICENSE).

***
