from abc import ABC, abstractmethod

class Membresia(ABC):
    """
    Clase base abstracta que define la estructura y comportamiento de una membresía.

    Atributos:
    ----------
    correo_suscriptor : str
        Correo electrónico del suscriptor.
    numero_tarjeta : str
        Número de tarjeta del suscriptor.
    """

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Inicializa una nueva instancia de Membresia.

        Parámetros:
        -----------
        correo_suscriptor : str
            Correo electrónico del suscriptor.
        numero_tarjeta : str
            Número de tarjeta del suscriptor.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        """
        Devuelve el correo electrónico del suscriptor.
        """
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        """
        Devuelve el número de tarjeta del suscriptor.
        """
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método abstracto para cambiar la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.
        """
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        """
        Crea una nueva membresía basada en el identificador proporcionado.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente.
        """
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

class Gratis(Membresia):
    """
    Clase que representa una membresía gratuita.

    Atributos de clase:
    -------------------
    costo : int
        Costo de la membresía.
    cantidad_dispositivos : int
        Cantidad máxima de dispositivos permitidos.
    """
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente, o la membresía actual si el identificador es inválido.
        """
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

class Basica(Membresia):
    """
    Clase que representa una membresía básica.

    Atributos de clase:
    -------------------
    costo : int
        Costo de la membresía.
    cantidad_dispositivos : int
        Cantidad máxima de dispositivos permitidos.
    """
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Inicializa una nueva instancia de Basica.

        Parámetros:
        -----------
        correo_suscriptor : str
            Correo electrónico del suscriptor.
        numero_tarjeta : str
            Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        """
        Cancela la suscripción actual y crea una membresía gratuita.

        Retorna:
        --------
        Gratis
            Nueva instancia de la membresía gratuita.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente, o la membresía actual si el identificador es inválido.
        """
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

class Familiar(Basica):
    """
    Clase que representa una membresía familiar.

    Atributos de clase:
    -------------------
    costo : int
        Costo de la membresía.
    cantidad_dispositivos : int
        Cantidad máxima de dispositivos permitidos.
    """
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente, o la membresía actual si el identificador es inválido.
        """
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        """
        Modifica el control parental de la membresía. Método a definir en el futuro.
        """
        pass

class SinConexion(Basica):
    """
    Clase que representa una membresía sin conexión.

    Atributos de clase:
    -------------------
    costo : int
        Costo de la membresía.
    """
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente, o la membresía actual si el identificador es inválido.
        """
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        """
        Incrementa la cantidad máxima de contenido disponible para ver sin conexión. Método a definir en el futuro.
        """
        pass

class Pro(Familiar, SinConexion):
    """
    Clase que representa una membresía Pro.

    Atributos de clase:
    -------------------
    costo : int
        Costo de la membresía.
    cantidad_dispositivos : int
        Cantidad máxima de dispositivos permitidos.
    """
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción del usuario a una nueva membresía.

        Parámetros:
        -----------
        nueva_membresia : int
            Identificador numérico de la nueva membresía solicitada.

        Retorna:
        --------
        Membresia
            Nueva instancia de la membresía correspondiente, o la membresía actual si el identificador es inválido.
        """
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Ejemplo de uso
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))  # <class '__main__.Gratis'>
b = g.cambiar_suscripcion(1)
print(type(b))  # <class '__main__.Basica'>
f = b.cambiar_suscripcion(2)
print(type(f))  # <class '__main__.Familiar'>
sc = f.cambiar_suscripcion(3)
print(type(sc))  # <class '__main__.SinConexion'>
pro = sc.cambiar_suscripcion(4)
print(type(pro))  # <class '__main__.Pro'>
g2 = pro.cancelar_suscripcion()
print(type(g2))  # <class '__main__.Gratis'>
