from flask import Flask, request, jsonify

app=Flask(__name__)

users=[]
# get all users
@app.route("/users",methods=["GET"])
def get_users():
  return jsonify(users), 200
#get single user
@app.route("/users/<int:user_id>",methods=["GET"])
def get_single_user(user_id):
  for user in users:
    if user ["id"]==user_id:
      return jsonify(user), 200
    
  return jsonify({"Error:user not found"}),400
# create user -POST
@app.route("/users",methods=["POST"])
def create_user():
  data=request.get_json()
  # validation
  if not data or "name" not in data or "email" not in data:
    return jsonify({"error":"invalid input"}), 400

  new_user = {
    "id":len(users) + 1,
     "name": data["name"],
    "email": data["email"]
  }
  users.append(new_user)
  print(users)
  
  return jsonify(new_user) ,201
# put -update user
@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
  data=request.get_json()
  for user in users:
    if user["id"]==user_id:
        user["name"]=data.get("name",user["name"])
        user["email"]=data.get("email",user["email"])
        return jsonify(user) , 200
    
  return jsonify({"error":"user not found"}) ,404
#Delete-remove user
@app.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
  for user in users:
    if user["id"]==user_id:
      users.remove(user)
      return jsonify({"message":"user deleted"}),200
    
  return jsonify({"error":"user not found"}) , 404

if __name__=="__main__":
 app.run(debug=True, port=5001)
