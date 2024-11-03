from flask import Flask, request, jsonify,render_template
import threading

app = Flask(__name__)

database = {
    "r4": {"user_id": "1", "name": "Ria", "email": "ria.bhargava@gmail.com"},
    "jdoe3": {"user_id": "2", "name": "John", "email": "john@example.com"}
}

@app.route("/")
def home():
    return render_template('index.html')

##this is the route of the user
@app.route("/getuser/<user_id>")
def get_user(user_id):
    if user_id in database:
        print("reached")
        user_data = database[user_id]
    else:
        user_data = {
            "user_id": user_id,
            "name": "John Doe",
            "email": "john.doe@gmail.com"
        }
        
    return jsonify(user_data), 200
##since we arent using the default get request, we have to specify
@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()

    if not data or "user_id" not in data:
        return jsonify({"error": "Missing user_id or data"}), 400
    if data["user_id"] in database:
        return jsonify({"error": "Already exists"}), 400
    
    print(data["user_id"])
    database[data["user_id"]] = data
    return jsonify(database), 201

@app.route("/patchuser", methods = ["PATCH"])
def patch_user():
    data = request.get_json()
    # with ##:
    # cond.wait()
    
    if not data or "user_id" not in data:
        return jsonify({"error": "No data provided"}), 400
    
    user = data["user_id"]
    if user not in database:
        return jsonify({"error": "Missing user_id or data"}), 400
    
    for key, value in data.items():
        if key != "user_id":  # Prevent changing the user_id itself
            database[user][key] = value

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)






# #put, get -> restful
# #acid -> non-restful

# ##post is idempotent means that if you do the same thing, get the same thing back
# ##takes something but wont always give the same result -> modify 

# ##flask is lightweight, less import, less compute

# from flask import Flask
# import threading

# app = Flask(__name__)



# if __name__ == "__main__":
#     ##can change port
#     # app.run(port=8081)
#     ##exposing the endpoint to the rest of the points
#     app.run(host='0.0.0.0')

##look into this
##cross origin resource sharing 

##two threads access the same object -> race condition
# def printThreadOne():
#     for _ in range(5):
#         print("Thread one")

# def printThreadTwo():
#     for _ in range(5):
#         print("Thread two")
    
# threadOne = threading.Thread(target=printThreadOne)

# threadTwo = threading.Thread(target=printThreadTwo)

# lock = threading.Lock()

# def x():
#     with lock:
#         for i in range(50):
#             print(i)

    
# threadOne = threading.Thread(target=x)
# threadTwo = threading.Thread(target=x)

# threadOne.start()
# threadTwo.start()

# ##to make it concurrent
# threadOne.join()
# threadTwo.join()



