from flask import Flask, render_template, request
import csv
submissions = []

csvfile = open('submissions.csv', 'w', newline='')
fieldnames = ['name', 'email', 'number', 'address']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    email = request.args.get('email')
    number = request.args.get('number')
    address = request.args.get('address')
    props = {
        "name" : name,
        "email" : email,
        "number" : number,
        "address" : address
    }
    submissions.append((name,email,number,address))
    return render_template("confirmation.html", data=props)


if __name__ == "__main__":
    app.run(debug=True,port=5000)
    print("hi")
    if len(submissions) > 0:
        for name, email, number, address in submissions:
            print(f"{name}, {email}, {number}, {address}")
            writer.writerow({'name': name, 'email': email, 'number': number, 'address': address})
