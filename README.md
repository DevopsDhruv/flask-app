# Simple Flask App for Testing Infrastructure

This project contains a simple Flask app to be used for testing infrastructure setups on the cloud.

## Overview

The Flask app is designed to demonstrate the basic functionality of deploying a web application on cloud infrastructure. It can be used to test different infrastructure setups, including two-tier and three-tier architectures.

## Deploy on Basic EC2 Instance

To deploy this Flask app on an EC2 instance, follow these steps:

1. **Create an EC2 instance**:
    ```bash
    git clone https://github.com/DevopsDhruv/EC2-Instance_with_terraform.git
    ```
    Read the `README.md` file form this repository to create an EC2 instance.

2. **SSH to EC2 instance and run the following commands to deploy the Flask app**:

    ```bash
    ssh-keygen
    ```

    Create ssh key and name it exactly `instance_key`
    ```bash
    ssh -i 'instance_key' ubuntu@Change_with_Instance_publicIP
    ```

3. **Install Docker and Docker Compose**:

    Inside your created EC2 instance, run these commands:

    ```bash
    git clone https://github.com/DevopsDhruv/Install-Docker.git

    cd Install-Docker

    chmod a+x Install_Docker.sh

    ./Install_Docker.sh

    cd ..
    ```

4. **Clone the Flask app**:

    ```bash
    git clone https://github.com/DevopsDhruv/flask-app.git

    cd flask-app
    ```

5. **Run `docker-compose_local.yml`**:

    ```bash
    docker-compose -f docker-compose_local.yml up --build -d
    ```

**Now you can access the Flask app at `instance_publicIP:5000`.**

## Check Data Inside MySQL Container

1. **Connect to the MySQL container**:

    ```bash
    mysql -h mysql -u admin -p
    Password: admin54321

    USE flaskapp;

    SELECT * FROM users;
    ```

## 
