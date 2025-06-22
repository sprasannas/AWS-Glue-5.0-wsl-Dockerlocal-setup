# AWS-Glue-5.0-wsl-Dockerlocal-setup

1.Install WSL stands for Windows Subsystem for Linux.

2.Install Docker Desktop.

3.To set up a local development environment for AWS Glue 5.0 jobs, pull the official Glue 5.0 image from Amazon's Elastic Container Registry (ECR):
            docker pull public.ecr.aws/glue/aws-glue-libs:5

            
*****Docker Image for Glue5.0******


<img width="745" alt="image" src="https://github.com/user-attachments/assets/5e6d0498-cd3e-446b-8c0f-2b1d2c3a7c6e" />


*****Compatable versions need to be installed for AWS Glue 5.0*****




<img width="948" alt="image" src="https://github.com/user-attachments/assets/758e7172-bf1a-4b96-a183-40c30d690b6b" />
<img width="939" alt="image" src="https://github.com/user-attachments/assets/144254f5-ed02-4fe3-94c4-8fd256553381" />



4. export WORKSPACE_LOCATION=/home/spras/gluetest
What it does: Sets the environment variable WORKSPACE_LOCATION to the path /home/spras/gluetest.

Purpose: Used to refer to the directory where your project or AWS Glue workspace files are stored.

Why it's useful: Instead of typing the full path every time, you can just use $WORKSPACE_LOCATION in your scripts or terminal.

5. export SCRIPT_FILE_NAME=sample.py
What it does: Sets the environment variable SCRIPT_FILE_NAME to the filename sample.py.

Purpose: Helps reference the Python script file dynamically.

Why it's useful: You can use this in automation scripts or command-line commands to run or copy files.

6. export PROFILE_NAME=default
What it does: Sets the environment variable PROFILE_NAME to default.

Purpose: Commonly used with AWS CLI or Boto3 to specify which AWS credentials profile to use (from ~/.aws/credentials).

Why it's useful: You might have multiple AWS profiles (e.g., dev, prod, default). This sets the one your script or session should use.

7.Running a Docker container that executes an AWS Glue 5.0 Spark job locally using spark-submit.
spras@spsrao:~$ docker run -it --rm \
    -v ~/.aws:/home/hadoop/.aws \
    -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
    -e AWS_PROFILE=$PROFILE_NAME \
    --name glue5_spark_submit \
    public.ecr.aws/glue/aws-glue-libs:5 \
    spark-submit /home/hadoop/workspace/$SCRIPT_FILE_NAME

8.To build a custom Docker image for your AWS Glue project using your local files
      docker build -t testproject/glue-sample:5 .


<img width="726" alt="image" src="https://github.com/user-attachments/assets/c9d4608b-59c7-4aef-9092-f1c023ac9118" />



9.Command runs a Docker container from the image testproject/glue-sample:5 that was previously built using your custom Dockerfile.
      docker run -it --rm testproject/glue-sample:5

