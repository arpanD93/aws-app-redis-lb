CODE  setup
==========
project/frontend/index.html;
project/backend/app.py;
project/utils/elasticache_interaction.py

This structure reflects the division of the code into frontend, backend, and utility components:

index.html: HTML file for the web interface.
app.py: Python file containing the Flask application code.
elasticache_interaction.py: Python file containing the code for interacting with Elasticache Redis.

AWS setup
============
Step 1: Set Up EC2 Instances
Launch EC2 Instances: Go to the EC2 dashboard, click on "Launch Instance," and select an Amazon Linux or Ubuntu Server. Choose the t2.micro instance type (eligible for the free tier).
Configure Security Groups: Create a new security group allowing HTTP (port 80) traffic for the web UI instance and allowing all traffic from the backend instance to the RDS instance.
SSH into Instances: Once the instances are running, SSH into each instance to configure them.

Step 2: Set Up Web UI and Backend
Install Dependencies: Install necessary software like Python, Flask (for the web UI), and any other dependencies your backend requires.
Code Deployment: Upload your web UI code to the web UI instance and backend code to the backend instance. You can use scp or git to transfer files.
Run the Applications: Start your Flask application on the web UI instance and your backend application on the backend instance.

Step 3: Set Up RDS Instance
Create RDS Instance: Go to the RDS dashboard, click on "Create database," and choose MySQL as the engine. Select the appropriate DB instance size and configure security settings.
Connect to RDS: Once the RDS instance is ready, note down the endpoint, username, and password. Configure your backend application to connect to this RDS instance using these credentials.

Step 4: Set Up Elasticache
Create Elasticache Cluster: Go to the ElastiCache dashboard, click on "Create," and choose Redis as the engine. Configure the cluster settings and security group.
Connect to Elasticache: Note down the endpoint of the Elasticache cluster. Configure your backend application to connect to this Elasticache cluster using the endpoint.

Deployment Steps:
===============
Deploy the frontend code on one EC2 instance:
Copy the index.html file to the EC2 instance.
Configure a web server (e.g., Nginx or Apache) to serve the static files.
Update the frontend code to include the IP address of the backend EC2 instance.
Deploy the backend code on another EC2 instance:
Copy the app.py file to the EC2 instance.
Install Python and Flask on the EC2 instance.
Run the Flask application on the EC2 instance.
Ensure that the security groups of both EC2 instances allow traffic between them on the necessary ports (e.g., port 5000 for the Flask application).
Access the frontend application by navigating to the public IP address or DNS name of the frontend EC2 instance in a web browser.
