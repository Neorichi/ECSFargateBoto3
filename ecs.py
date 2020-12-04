# -*- coding: utf-8 -*-
import json
import datetime
import requests
import boto3
import time

def initClient(access_key,secret_key,region):
    return boto3.client(
	    'ecs',
	    aws_access_key_id=access_key,
	    aws_secret_access_key=secret_key,
	    region_name=region
	)


def createClusterECS(ecsClient,cluserName):
    response = ecsClient.create_cluster(clusterName=cluserName)
    print(response)

def createTaskECS(ecsClient,cluserName,taskName,container_name,image,containerPort,cmd=False):
    # TASK DEFINTION
    responseTask = ecsClient.register_task_definition(
        family=taskName,
        #Creating role ECSTaskExecutionRole to sharing Task
        executionRoleArn="ECSTaskExecutionRole",
        taskRoleArn="ECSTaskExecutionRole",
        containerDefinitions=[
        {
          "name": container_name,
          "image": image,
          "cpu": 512,
          "memory": 1024,
          # Optional (it's not need it beacause we are using CMD [ "python", "./app/main.py" ] in the Dockerfile)
          #"entryPoint": ["sh", "-c"],
    	  #'command': [cmd],
          "portMappings": [
              {
              'containerPort': containerPort,
              'protocol': 'tcp'
              },
          ],

        },
        ],
        networkMode="awsvpc",
        requiresCompatibilities=['FARGATE'],
        cpu=".5vCPU",
        memory="1GB"
    )

    print(responseTask)
    #Get 20seconds to create service well
    print("Sleeping 20 secs")
    time.sleep(20)


def createServiceECS(ecsClient,cluserName,serviceName,taskName):
	responseService = ecsClient.create_service(
	    cluster=cluserName,
	    serviceName=serviceName,
	    taskDefinition=taskName,
	    desiredCount=1,
	    launchType="FARGATE",
	    deploymentConfiguration={
	        'maximumPercent': 300,
	        'minimumHealthyPercent': 50
	    },
	    networkConfiguration={
    	    'awsvpcConfiguration': {
    	        'subnets': [
    	            #'subnet-XXXXXXXXXXXXXXX',
    	            #'subnet-XXXXXXXXXXXXXXX',
    	            'subnet-XXXXXXX'
    	        ],

    	        'securityGroups': ['sg-XXXXXXXXX'],
    			'assignPublicIp': 'ENABLED'
    	    }
	    },
	)
	print(responseService)



if __name__ == "__main__":
    accessKey = "XXXXXXXXXXXX"
    secretKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    region = "us-east-1"
    cluserName= "Cluster-demo"
    taskName= "Task-demo"
    serviceName= "Service-demo"
    image = "XXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/image-demo:latest"
    ecsClient = initClient(accessKey,secretKey,region)
    createClusterECS(ecsClient,cluserName)
    createTaskECS(ecsClient,cluserName,taskName,cluserName,image,80,cmd=False)
    createServiceECS(ecsClient,cluserName,serviceName,taskName)
