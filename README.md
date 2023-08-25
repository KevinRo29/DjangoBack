# DjangoBack

DjangoBack - API is a management system for online stores that allows you to manage products, perform login operations and take advantage of the capabilities of a backend developed in Python using the Django framework.

## Project Description

DjangoBack is an application that allows you to perform the following actions:

- **Product management**: Create, update and delete products in your inventory. Each product can include details such as name, description, price and category.

- **Login and security**: Provides a secure authentication system that allows users to register, login and manage their accounts. This ensures that only authorized users can access the administration functions.

- **Dynamic backend**: The backend developed in Django provides a smooth and engaging user experience. Products are presented intuitively and users can perform various actions quickly and easily.

- **Efficient database**: Using SQLite3, the project efficiently stores product information, user accounts and other entities relevant to the operation of the online store.

This project is ideal for those looking for an out-of-the-box solution to create their own online store. Whether you are a developer looking to learn about web application development with Django and Python, or an entrepreneur looking to launch your online store, DjangoBack gives you a solid foundation to build on.

## Technologies

The project is developed using the following technologies:

- **Django**: Django is a high-level web framework for Python that encourages rapid development and clean, pragmatic design. It is a free and open source framework, released under the BSD license.

- **SQLite3**: SQLite is a relational database management system contained in a C library. Unlike many other database management systems, SQLite is not a client-server database engine. Instead, it is embedded in the final program.

## Requirements

Before you start using this project, make sure you have Python and Django installed. If you don't already have them, you can download them from the following links:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)

## Installation

Follow these steps to install the project in your local environment:

1. Clone the repository on your local machine:

```bash
git clone https://github.com/KevinRo29/DjangoBack.git
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

## Notes

- To see the admin panel, go to the following URL: http://127.0.0.1:8000/admin/login/?next=/admin/

- When a user is created, it is stored as a non-active record, therefore, to change a user to active, do the following:

1. In the terminar run the following command:

```bash
python manage.py shell
```

2. Once in the shell, run the following commands:

```bash
from Apps.Authenticate.models import UserAccount
user = UserAccount.objects.get(email='your-email')
user.is_active = True
user.save()
```

3. Exit the shell
    
```bash
exit()
```

## Usage

### Main functionalities

1. Log in to the application using your user credentials.

2. Once authenticated, access the product management section.

3. Here you can see the list of existing products. You can create new products, edit existing ones and delete products you no longer need.

### Customization and expansion

If you want to customize or expand the functionality of the application, you can:

1. Add news characteristics to the Backend using Django and Python.

2. Modify and improve the business logic in the backend.

3. Improve security through two-factor authentication.

4. Implementar un sistema de calificaciones y reseñas para los productos

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
