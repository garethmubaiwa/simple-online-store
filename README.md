BookVerse – Online Book Store
Django, Python, Bootstrap

BookVerse is a modern online bookstore built with Django. It lets users browse books, search titles, manage a cart, and create accounts.

Features

* Product catalog: Browse books with images and descriptions
* Search: Find books by title, description, or category
* Shopping cart: Add and remove items, adjust quantities
* User accounts: Registration, login, and profiles
* Session handling: Cart persists across browser sessions
* Responsive layout: Works across desktop and mobile
* Interface: Clean, minimal design

Technology Stack

* Backend: Django 4.2, Python 3.8+
* Database: SQLite (development), PostgreSQL (production)
* Frontend: HTML5, CSS3, JavaScript
* Styling: Custom CSS (Grid and Flexbox)
* Authentication: Django auth system
* File handling: Django FileSystemStorage

Installation

Prerequisites

* Python 3.8+
* pip

Setup

Clone the repository
git clone [https://github.com/yourusername/bookverse.git](https://github.com/yourusername/bookverse.git)
cd bookverse

Create a virtual environment
python -m venv venv
source venv/bin/activate
(On Windows: venv\Scripts\activate)

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py migrate

Create a superuser
python manage.py createsuperuser

Run the server
python manage.py runserver

Access the app

* Main site: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Project Structure

bookverse/
├── main/        Homepage and base templates
├── products/    Product catalog
├── users/       Authentication and profiles
├── orders/      Cart and order logic
├── store/       Project settings
├── media/       Uploaded images
├── static/      CSS, JS, assets
└── manage.py    Management script

Usage (current state)

Customers

* Browse books on the products page
* Use search to find titles
* Add items to cart
* View cart from the cart icon
* Create an account to save details

Administrators

* Access /admin with superuser credentials
* Add, edit, or remove books
* View carts and orders
* Manage user accounts and permissions

Notes

* SQLite is used by default. Update settings.py for production.

Contributing

Contributions are welcome.

* Fork the repository
* Create a branch (git checkout -b feature/AmazingFeature)
* Commit changes (git commit -m "Add feature")
* Push (git push origin feature/AmazingFeature)
* Open a pull request

License

MIT License. See the LICENSE file for details.

Developer
Gareth Mubaiwa
[garethmubaiwa18@gmail.com](mailto:garethmubaiwa18@gmail.com)

Acknowledgments

* Django documentation
* Font Awesome (icons)
* Coolors (color palettes)
* Bootstrap 5 (design references)
