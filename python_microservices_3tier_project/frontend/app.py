
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

SERVICES = {
    "users": "http://user_service:5001/items",
    "products": "http://product_service:5002/items",
    "orders": "http://order_service:5003/items"
}

def get_all_data():
    """Fetch data from all services"""
    try:
        users = requests.get(SERVICES["users"], timeout=2).json()
    except:
        users = []
    
    try:
        products = requests.get(SERVICES["products"], timeout=2).json()
    except:
        products = []
    
    try:
        orders = requests.get(SERVICES["orders"], timeout=2).json()
    except:
        orders = []
    
    return users, products, orders

@app.route("/")
def dashboard():
    users, products, orders = get_all_data()
    return render_template("dashboard.html", users=users, products=products, orders=orders)

@app.route("/users", methods=["GET", "POST"])
def users_page():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            requests.post(SERVICES["users"], json={"name": name})
        return redirect("/users")
    
    users, _, _ = get_all_data()
    return render_template("users.html", users=users)

@app.route("/products", methods=["GET", "POST"])
def products_page():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            requests.post(SERVICES["products"], json={"name": name})
        return redirect("/products")
    
    _, products, _ = get_all_data()
    return render_template("products.html", products=products)

@app.route("/orders", methods=["GET", "POST"])
def orders_page():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            requests.post(SERVICES["orders"], json={"name": name})
        return redirect("/orders")
    
    _, _, orders = get_all_data()
    return render_template("orders.html", orders=orders)

@app.route("/about")
def about():
    return render_template("about.html")

# Legacy routes for backward compatibility
@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    requests.post(SERVICES["users"], json={"name": name})
    return redirect("/users")

@app.route("/add_product", methods=["POST"])
def add_product():
    name = request.form.get("name")
    requests.post(SERVICES["products"], json={"name": name})
    return redirect("/products")

@app.route("/add_order", methods=["POST"])
def add_order():
    name = request.form.get("name")
    requests.post(SERVICES["orders"], json={"name": name})
    return redirect("/orders")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
