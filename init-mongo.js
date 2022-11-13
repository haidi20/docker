db = db.getSiblingDB('mongodb');

db.createCollection('sample_collection');

db.createUser({
    user: "root",
    pwd: "root",
    roles: [{
        role: "readWrite",
        db: "mongodb"
    }]
});