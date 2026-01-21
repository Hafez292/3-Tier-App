from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure PostgreSQL
db_user = os.getenv('POSTGRES_USER', 'postgres')
db_pass = os.getenv('POSTGRES_PASSWORD', 'password')
db_host = os.getenv('POSTGRES_HOST', 'db')
db_name = os.getenv('POSTGRES_DB', 'mydatabase')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Sample table for demonstration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# API routes
@app.route('/')
def hello():
    return jsonify(message='Hello from Flask!')

@app.route('/redis')
def redis_test():
    redis_client.set('foo', 'bar')
    value = redis_client.get('foo')
    return jsonify(redis_value=value)

@app.route('/users')
def list_users():
    users = User.query.all()
    return jsonify(users=[user.name for user in users])

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
