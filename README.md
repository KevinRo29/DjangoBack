# Django-Vue Store Backend

Django-Vue Store is an online store management system that allows you to manage products, perform login operations and leverage the capabilities of a backend developed in Python using the Django framework. Together with the frontend developed in Vue (JavaScript) and an elegant design in Tailwind CSS, this project provides a complete solution for creating and managing an online store.

## Project description

Django-Vue Store is an e-commerce application that allows you to perform the following actions:

- **Product management**: Create, update and delete products in your inventory. Each product can include details such as name, description, price and category.

- **Login and security**: Provides a secure authentication system that allows users to register, login and manage their accounts. This ensures that only authorized users can access administration functions.

- **Attractive and dynamic frontend**: The frontend developed in Vue.js offers a smooth and engaging user experience. Products are presented in an intuitive way, and users can perform actions such as adding products to cart and shopping efficiently.

- **Modern design**: The interface design is based on Tailwind CSS, which provides a modern and responsive look and feel. This ensures that the application looks and works optimally on different devices and screen sizes.

- **Efficient database**: Using SQLite3, the project efficiently stores product information, user accounts and other entities relevant to the operation of the online store.

This project is ideal for those looking for an out-of-the-box solution to create their own online store. Whether you are a developer looking to learn about web application development with Django and Vue, or an entrepreneur looking to launch your online store, TiendaVBack provides you with a solid foundation to build upon.

## Technologies

The project is developed using the following technologies:

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is a free and open-source framework, released under the BSD license.

- **Vue.js**: Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.

- **Tailwind CSS**: Tailwind CSS is a utility-first CSS framework for rapidly building custom user interfaces.

- **SQLite3**: SQLite is a relational database management system contained in a C library. In contrast to many other database management systems, SQLite is not a client–server database engine. Rather, it is embedded into the end program.

## Requirements

Before you start using this project, make sure you have Python and Django installed. If you don't have them yet, you can download them from the following links:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)

## Installation

Follow these steps to install the project in your local environment:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/KevinRo29/Django-Vue-Store
```

2. Install the project dependencies:

```bash
pip install -r requirements.txt
```

3. Run the migrations to create the database:

```bash
python manage.py migrate
```

4. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## Usage

### Main functionalities

1. Log in to the application using your user credentials.

2. Once authenticated, access the product management section.

3. Here you can see the list of existing products. You can create new products, edit existing ones and delete products you no longer need.

### Customization and expansion

If you want to customize or expand the functionality of the application, you can:

1. Add new features to the frontend using Vue.js.

2. Modify and improve the business logic on the backend using Django and Python.

3. Improve security through two-factor authentication.

4. Implement a ratings and reviews system for products.

Feel free to explore and experiment with the code to adapt it to your specific needs!

## Contributing

Contributions are always welcome! If you want to collaborate with the project, you can:

1. Create a new branch with the name of your feature:

```bash
git checkout -b feature/MyFeature
```

2. Commit your changes:

```bash
git commit -m "My feature"
```

3. Push your changes to the branch:

```bash
git push origin feature/MyFeature
```

4. Open a pull request and describe the changes you have made.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

_This portfolio is curated by Kevin Romero. Feel free to contact me at kevinro0829@gmail.com for any inquiries or collaborations._
