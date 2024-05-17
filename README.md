# Desafío Guiado: Estructura de clases para membresías de una aplicación de streaming

En este desafío, se pondrá a prueba los conocimientos sobre herencia de clases y sobreescritura de métodos para desarrollar la estructura de clases que permita crear y gestionar membresías de usuarios suscriptores en una aplicación de streaming de videos de películas y series chilenas.

## Descripción

Como programador backend contratado por una empresa de streaming de videos chilenos, se te encomienda diseñar la estructura de clases para gestionar las membresías de los usuarios suscriptores. Se requieren cinco tipos de membresía: Gratis, Básica, Familiar, Sin Conexión y Pro.

En este contexto de diseño, se te solicita considerar que la creación de cada membresía requiere información básica del suscriptor, como su correo electrónico y número de tarjeta, ambos representados como texto. Además, ciertos tipos de membresía otorgan días de regalo al crearse, un valor que, aunque fijo por ahora, podría modificarse en el futuro.

En cuanto a las funcionalidades, todas las membresías deben permitir cambiar la suscripción, lo que implica generar una nueva membresía del tipo especificado, manteniendo intactos el correo electrónico y el número de tarjeta de la membresía original.

## Requerimientos

- En el archivo membresia.py, crear la clase base que defina los atributos de instancia y comportamientos comunes a todas las membresías.

- Crear la clase para instancias de membresías de tipo Gratis, que herede de la clase base. Esta clase debe definir los atributos y comportamientos específicos de las membresías Gratis.

- Crear la clase para instancias de membresías de tipo Básica, heredando de la clase base. Esta clase debe definir los atributos y comportamientos específicos de las membresías Básicas.

- Crear la clase para instancias de membresías de tipo Familiar, heredando de la clase base. Esta clase debe definir los atributos y comportamientos específicos de las membresías Familiares.

- Crear la clase para instancias de membresías de tipo Sin Conexión, heredando de la clase base. Esta clase debe definir los atributos y comportamientos específicos de las membresías Sin Conexión.

- Crear la clase para instancias de membresías de tipo Pro, heredando de la clase base. Esta clase debe definir los atributos y comportamientos específicos de las membresías Pro.

## Empezando 🚀

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Clonar el repositorio

```bash
git clone [git@github.com:Vaniakmt/desafioMembresia.git](https://github.com/Vaniakmt/desafioMembresia.git)
```

### Prerrequisitos 📋

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo: Ubuntu 20.04 o Windows 10
- Lenguaje de programación : Python 3.8 o superior
- Git (para control de versiones)
- Pip (administrador de paquetes de Python)
- IDE o editor de texto: Visual Studio Code, PyCharm
