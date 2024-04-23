import redis

# Connect to Elasticache Redis
def connect_to_redis():
    r = redis.Redis(host='your-elasticache-endpoint', port=6379, db=0)
    return r

# Example usage
def example_redis_interaction():
    r = connect_to_redis()
    r.set('key', 'value')
    value = r.get('key')
    print(value)  # Output: b'value'

example_redis_interaction()
