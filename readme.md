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
Frontend Setup (EC2 Instance 1):
--------------------------------
Install Apache: SSH into your EC2 instance and install Apache web server.

```bash
sudo yum update -y ;
sudo yum install httpd -y;
Copy Frontend Code: Transfer your frontend code (including index.html) to the /var/www/html directory.


Configure Apache: Configure Apache to serve your frontend files. Create or edit the Apache configuration file (/etc/httpd/conf/httpd.conf) and add the following configuration:
apache


<Directory "/var/www/html">
    AllowOverride All
    Require all granted
</Directory>

Start Apache: Start the Apache web server and enable it to start on boot.

sudo systemctl start httpd
sudo systemctl enable httpd

Open Ports: Open port 80 in the security group of your EC2 instance to allow HTTP traffic.

Backend Setup (EC2 Instance 2):
--------------------
Install Python and Flask: SSH into your second EC2 instance and install Python and Flask.


sudo yum update -y
sudo yum install python3 python3-pip -y
sudo pip3 install flask

Copy Backend Code: Transfer your backend code (e.g., app.py) to the desired directory on your EC2 instance.
Run Flask Application: Run your Flask application specifying the host and port.


export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000

Open Ports: Open port 5000 in the security group of your EC2 instance to allow incoming traffic to your Flask application.
Set Up Apache as Reverse Proxy (Optional): You can set up Apache as a reverse proxy to forward requests to your Flask application. Install the necessary Apache modules and configure the virtual host:


sudo yum install mod_wsgi

Then, create a virtual host configuration file (e.g., /etc/httpd/conf.d/backend.conf) with the following content:
apache

<VirtualHost *:80>
    ServerName backend.example.com
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/
</VirtualHost>

Replace backend.example.com with your actual domain name or IP address. After creating the file, restart Apache:

sudo systemctl restart httpd

Now, you should have your frontend hosted on one EC2 instance with Apache serving the static files, and your backend hosted on another EC2 instance with Flask running the backend application. Adjust the configurations as needed based on your specific requirements and environment.



