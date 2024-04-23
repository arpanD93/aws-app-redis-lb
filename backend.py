from flask import Flask
import pymysql
import redis

app = Flask(__name__)

# Connect to RDS MySQL
def connect_to_mysql():
    connection = pymysql.connect(host='your-rds-endpoint',
                                user='your-username',
                                password='your-password',
                                database='your-database',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

# Connect to Elasticache Redis
def connect_to_redis():
    r = redis.Redis(host='your-elasticache-endpoint', port=6379, db=0)
    return r

@app.route('/')
def index():
    return 'Welcome to the Backend'

@app.route('/mysql')
def mysql_interaction():
    connection = connect_to_mysql()
    # Use the connection to interact with the MySQL database
    return 'Interacted with MySQL'

@app.route('/redis')
def redis_interaction():
    r = connect_to_redis()
    # Use the Redis client to interact with the Elasticache cluster
    return 'Interacted with Redis'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
