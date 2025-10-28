# BookVerse - Online Book Store

![Django](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple)

A modern, fully-featured online book store built with Django. BookVerse allows users to browse books, search for titles, add items to cart, and create accounts.

![BookVerse Screenshot](https://via.placeholder.com/800x400/4361ee/ffffff?text=BookVerse+Online+Book+Store)

## 🚀 Features

- **📚 Product Catalog** - Browse all available books with images and descriptions
- **🔍 Advanced Search** - Search books by title, description, or category
- **🛒 Shopping Cart** - Add/remove items with quantity management
- **👤 User Authentication** - Register, login, and user profiles
- **💳 Secure Sessions** - Persistent cart across browser sessions
- **📱 Responsive Design** - Works perfectly on all devices
- **🎨 Modern UI** - Clean, professional interface

## 🛠️ Technology Stack

- **Backend**: Django 4.2, Python 3.8+
- **Database**: SQLite (Development), PostgreSQL (Production-ready) 
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Grid & Flexbox
- **Authentication**: Django Auth System
- **File Handling**: Django FileSystemStorage for images

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bookverse.git
   cd bookverse

2. **Create virtual environment**
    '''bash
    python -m venv venv
    source venv/bin/activate  #On Windows: venv\Scripts\activate

3. **Install dependences**
    '''bash
    pip install -r requirements.txt

4. **Run migrations**
    '''bash
    python manage.py migrate

5. **Create super_user**
    '''bash
    python manage.py createsuperuser

6. **Run development server**
    '''bash
    python manage.py runserver

7.  **Access the application**
    Main site: http://127.0.0.1:8000
    Admin panel: http://127.0.0.1:8000/admin

🗂️ Project Structure

bookverse/
├── main/                 # Homepage and base templates
├── products/            # Product catalog functionality
├── users/               # Authentication and user profiles
├── orders/              # Shopping cart and order management
├── store/               # Django project settings
├── media/               # Uploaded product images
├── static/              # Static files (CSS, JS, images)
└── manage.py           # Django management script


🎯 Usage (at current development stage)

For Customers
--Browse Books: Visit the products page to see all available books
--Search: Use the search bar to find specific titles
--Add to Cart: Click "Add to Cart" on any product
--View Cart: Click the cart icon to review your selections
--Create Account: Register to save your information

For Administrators
--Access Admin Panel: Visit /admin and login with superuser credentials
--Manage Products: Add, edit, or remove books from the catalog
--View Orders: Monitor customer carts and orders
--User Management: Manage user accounts and permissions

#####The project uses SQLite by default. For production, update settings.py


🤝 Contributing
I welcome contributions, updates and advice to make it better and cleaner! Please follow these steps:

Fork the project
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Developer
Gareth Mubaiwa 
Email: garethmubaiwa18@gmail.com

🙏 Acknowledgments
Django Documentation
Inspired by modern e-commerce platforms
Icons from Font Awesome
Color palette from Coolors.co
Color schemes from bootstrap 5
