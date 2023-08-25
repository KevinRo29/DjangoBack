# DjangoBack - Backend para Tienda en Línea

DjangoBack es un sistema de gestión para tiendas en línea que te permite administrar productos, realizar operaciones de inicio de sesión y aprovechar las capacidades de un backend desarrollado en Python utilizando el framework Django. Con un diseño elegante en Tailwind CSS, este proyecto proporciona una solución completa para crear y administrar una tienda en línea.

## Descripción del Proyecto

DjangoBack es una aplicación de comercio electrónico que te permite realizar las siguientes acciones:

- **Gestión de productos**: Crea, actualiza y elimina productos en tu inventario. Cada producto puede incluir detalles como nombre, descripción, precio y categoría.

- **Inicio de sesión y seguridad**: Proporciona un sistema de autenticación seguro que permite a los usuarios registrarse, iniciar sesión y gestionar sus cuentas. Esto asegura que solo los usuarios autorizados puedan acceder a las funciones de administración.

- **Backend atractivo y dinámico**: El backend desarrollado en Django ofrece una experiencia de usuario fluida y atractiva. Los productos se presentan de manera intuitiva y los usuarios pueden realizar acciones como agregar productos al carrito y comprar de manera eficiente.

- **Diseño moderno**: El diseño de la interfaz se basa en Tailwind CSS, lo que proporciona un aspecto moderno y receptivo. Esto asegura que la aplicación luzca y funcione de manera óptima en diferentes dispositivos y tamaños de pantalla.

- **Base de datos eficiente**: Utilizando SQLite3, el proyecto almacena eficientemente la información de los productos, las cuentas de usuario y otras entidades relevantes para el funcionamiento de la tienda en línea.

Este proyecto es ideal para aquellos que buscan una solución lista para usar para crear su propia tienda en línea. Ya seas un desarrollador que busca aprender sobre el desarrollo de aplicaciones web con Django y Python, o un emprendedor que busca lanzar su tienda en línea, DjangoBack te proporciona una base sólida sobre la cual construir.

## Tecnologías

El proyecto está desarrollado utilizando las siguientes tecnologías:

- **Django**: Django es un framework web de alto nivel para Python que fomenta el desarrollo rápido y un diseño limpio y pragmático. Es un framework de código abierto y gratuito, lanzado bajo la licencia BSD.

- **SQLite3**: SQLite es un sistema de gestión de bases de datos relacionales contenido en una biblioteca C. A diferencia de muchos otros sistemas de gestión de bases de datos, SQLite no es un motor de base de datos cliente-servidor. En cambio, está incrustado en el programa final.

## Requisitos

Antes de comenzar a usar este proyecto, asegúrate de tener instalados Python y Django. Si aún no los tienes, puedes descargarlos desde los siguientes enlaces:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)

## Instalación

Sigue estos pasos para instalar el proyecto en tu entorno local:

1. Clona el repositorio en tu máquina local:

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
