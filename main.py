from operator import itemgetter
import os, ast
from flask import Flask, flash, jsonify, render_template, request, redirect, send_from_directory, session, url_for
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayah123'
CART_FILE = 'cart.json'
try:
    os.remove('cart.json')
    print('cart.json file removed')
except FileNotFoundError:
    pass
movies =[
 {
 'id': 1,
 'title': 'Her',
 'image': '1.jpeg',
 'release_year': '2013',
 'genre': 'Romance',
 'running_time': '2h 6m',
 'director': 'Spike Jonze (October 22, 1969)',
 'lead_actors': 'Joaquin Phoenix (October 28, 1974) and Amy Adams (August 20, 1974)',
 'minor_character': 'Rooney Mara (April 17, 1985)',
 'producers': 'Spike Jonze (October 22, 1969) and Megan Ellison (January 31, 1986)',
 'studio': 'Annapurna Pictures (Address: 812 N Robertson Blvd, West Hollywood, CA)',
 'price': 50,
 'availability': 'Available'
 },
 {
 'id': 2,
 'title': 'Star Wars',
 'image': '2.jpeg',
 'release_year': '2019',
 'running_time': '2h 35m',
 'director': 'J.J. Abrams (June 27, 1966)',
 'lead_actors': 'Mark Hamill (September 25, 1951) and Harrison Ford (July 13, 1942)',
 'minor_character': 'Jake Matthew (August 19, 1994)',
 'producers': 'George Lucas (May 14, 1944) and Gary Kurtz (July 27, 1940)',
 'studio': 'Lucasfilm Ltd (Address: 1110 Gorgas Avenue San Francisco, CA 94129 USA)',
 'price': 50,
 'availability': 'Available'
 },
 {
 'id': 3,
 'title': 'Storm',
 'image': '3.jpeg',
 'release_year': '2017',
 'genre': 'Action',
 'running_time': '1h 49m',
 'director': 'Dean Devlin (August 27, 1962)',
 'lead_actors': 'Davy Gomez (November 11, 2003) and Juna de Leeuw (2001)',
 'minor_character': 'Golda de Leon (October 2006)',
 'producers': 'Katleen Goossens (May 23, 1976)',
 'studio': 'Rinkel Film (Address: Veemarkt 180, 1019 DGAmsterdam, Netherlands)',
 'price': 50,
 'availability': 'Available'
 },
 {
 'id': 4,
 'title': '1917',
 'image': '4.jpeg',
 'release_year': '2019',
 'genre': 'Drama',
 'running_time': '1h 59m',
 'director': 'Sam Mendes (August 1, 1965)',
 'lead_actors': 'George MacKay (March 13, 1992) and Richard Madden (June 18, 1986)',
 'minor_character': 'Colin Firth (September 10, 1960)',
 'producers': 'Sam Mendes (August 1, 1965) and Pippa Harris (March 27, 1967)',
 'studio': 'Neal Street Productions (Address: 26-28 Neal St Fl 1, London, Greater London, WC2H 9QQ, United Kingdom)',
 'price': 50,
 'availability': 'Available'
 },
 {
 'id': 5,
 'title': 'Avengers',
 'image': '5.jpeg',
 'release_year': '2012',
 'genre': 'Science fiction',
 'running_time': '2h 23m',
 'director': 'Joss Whedon (June 23, 1964)',
 'lead_actors': 'Robert Downey (April 4, 1965) and Chris Evans (June 13, 1981)',
 'minor_character': 'Scarlett Johansson (November 22, 1984)',
 'producers': 'Kevin Feige (June 2, 1973)',
 'studio': 'Marvel Studios LLC (Address: 500 S Buena Vista St, Burbank, CA)',
 'price': 50,
 'availability': 'Not Available'
 }
 ]
@app.route('/')
def index():
    return render_template('index.html', movies=movies)
def load_cart():
    cart_file_path = "cart.json" # Update with the correct file path
    try:
        with open(cart_file_path, "r") as file:
            try:
                cart = json.load(file)
                # Convert movie IDs from strings to integers
                cart = {int(movie_id): data for movie_id, data in cart.items()}
            except json.JSONDecodeError:
                cart = {}
    except FileNotFoundError:
        cart = {}
    return cart
def save_cart(cart):
    cart_file_path = "cart.json" # Update with the correct file path
 
    with open(cart_file_path, 'w') as file:
        json.dump(cart, file)
 
# @app.route('/cart')
# def cart():
#     movies_in_cart = []
#     cart = load_cart()
#     name = session.get('name', '')
#     email = session.get('email', '')
#     phone = session.get('phone', '')
#     address = session.get('address', '')
#     # Retrieve movie details based on movie_id
    
#     for movie_id, quantity in cart.items():
#         for movie in movies:
#             if movie['id'] == int(movie_id):
#                 movie_details = {
#                 'id': movie['id'],
#                 'title': movie['title'],
#                 'image': movie['image'],
#                 'price': movie['price'],
#                 'quantity': quantity # Store the quantity from the cart directly
#                 }
#                 movies_in_cart.append(movie_details)
#                 break
#     total_amount=0
#     for item in movies_in_cart:
#         total_amount = total_amount + float(item['price']) * item['quantity']
#     return render_template("cart.html", items_purchased=movies_in_cart, total_amount=total_amount, name=name, email=email, phone=phone, address=address)

@app.route('/cart')
def cart():
    movies_in_cart = []
    cart = load_cart()
    name = session.get('name', '')
    email = session.get('email', '')
    phone = session.get('phone', '')
    address = session.get('address', '')

    # Retrieve movie details based on movie_id
    for movie_id, item in cart.items():
        movie = next((m for m in movies if m['id'] == int(movie_id)), None)
        if movie:
            movie_details = {
                'id': movie['id'],
                'title': movie['title'],
                'image': movie['image'],
                'price': movie['price'],
                'quantity': item['quantity'] # Store the quantity from the cart directly
            }
            movies_in_cart.append(movie_details)

    total_amount = sum(float(movie['price']) * int(movie['quantity']) for movie in movies_in_cart)
    return render_template("cart.html", items_purchased=movies_in_cart, total_amount=total_amount, name=name, email=email, phone=phone, address=address)

def calculateTotalAmount(movies_in_cart):
    total_amount = 0
    for item in movies_in_cart:
        try:
            quantity = int(item.get('quantity', 1))
        except (ValueError, TypeError):
            quantity = 1
        price = float(item.get('price', 0)) 
        total_amount += quantity * price
    return total_amount


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    movie_id = request.form['movie_id']
    movie_title = request.form['movie_title']
    movie_price = request.form['movie_price']
    
    # Load cart from file
    cart = load_cart()
    movie_id_int = int(movie_id)
    
    # Retrieve the movie based on movie_id
    movie = next((m for m in movies if m['id'] == movie_id_int), None)
    
    # Check if the movie is available
    if movie and movie['availability'] == 'Available':
        if movie_id_int in cart:
            cart[movie_id_int]['quantity'] = int(cart[movie_id_int]['quantity']) + 1
        else:
            cart[movie_id_int] = {
                'title': movie_title,
                'price': int(movie_price),
                'quantity': 1
            }
    
        # Save updated cart to file
        save_cart(cart)
    
        return 'Item is available and added successfully to the cart'
    else:
        return 'Item is not available'


@app.route('/removeFromCart', methods=['POST'])
def remove_from_cart():
    movie_id = int(request.form.get('movieId'))
    cart = load_cart()
    
    if movie_id in cart:
        cart.pop(movie_id)
        save_cart(cart)
        
        response = {
        'success': True,
        'message': 'Item removed from cart successfully'
        }
    else:
        response = {
        'success': False,
        'message': 'Item not found in cart'
        }
    return render_template('cart.html')
def calculate_total_price(movies):
    total_price = 0
    for movie in movies:
        total_price += total_price + float(movie['price']) * int(movie['quantity'])
    return total_price

#checkout button 
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
    
    # Clear the cart after successful checkout
        try:
            os.remove(CART_FILE)
            print(f'{CART_FILE} file removed')
        except FileNotFoundError:
            pass
        
        return redirect('/checkout?name={}&email={}&phone={} &address={}'.format( name, email, phone, address))
        
    cart = load_cart()
    items_purchased = []
    # Retrieve detailed item information from the cart
    for movie_id, item in cart.items():
        for movie in movies:
            if movie['id'] == int(movie_id):
                item_details = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'image': movie['image'],
                    'price': item['price'],
                    'quantity': item['quantity']
                }
                items_purchased.append(item_details)
                break
    # Calculate the total price
    print(f"Items Purchased: {items_purchased}")
    total_price = 0

    for item in items_purchased:
        total_price = total_price + float(item['price']) * int(item['quantity'])

    # Retrieve the user information from the query parameters
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    phone = request.args.get('phone', '')
    address = request.args.get('address', '')
    return render_template('checkout.html',items_purchased=items_purchased, total_price=total_price,name=name, email=email, phone=phone, address=address)
if __name__ == '__main__':
 app.run(port=3300)
