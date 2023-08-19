class Tipo:
    def __init__(self, **kwargs):
        self.nombre = 'generico'
        self.dam = []
        self.recibed = []
        self.recibem = []
        self.dad = []
        self.da0 = []
        self.recibe0 = []
        for k, v in kwargs.items():
            setattr(self, k, v)
    def __repr__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    def __eq__(self, other):
        return self.nombre == other.nombre
    def get_nombre(self):
        return self.nombre
    def get_dam(self):
        return [x().get_nombre() for x in self.dam]
    def get_recibed(self):
        return [x().get_nombre() for x in self.recibed]
    def get_recibem(self):
        return [x().get_nombre() for x in self.recibem]
    def get_dad(self):
        return [x().get_nombre() for x in self.dad]
    def get_recibe0(self):
        return [x().get_nombre() for x in self.recibe0]


class Normal(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Normal"
        self.dam = [Roca, Acero]
        self.recibed = [Pelea]
        self.da0 = [Fantasma]
        self.recibe0 = [Fantasma]


class Pelea(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Pelea"
        self.dam = [Volador, Veneno, Bicho, Psiquico, Hada]
        self.recibed = [Volador, Psiquico, Hada]
        self.recibem = [Roca, Bicho, Siniestro]
        self.dad = [Normal, Roca, Acero, Hielo, Siniestro]
        self.da0 = [Fantasma]


class Volador(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Volador"
        self.dam = [Roca, Acero, Electrico]
        self.recibed = [Roca, Electrico, Hielo]
        self.recibem = [Pelea, Bicho, Planta]
        self.dad = [Pelea, Bicho, Planta]
        self.recibe0 = [Tierra]


class Veneno(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Veneno"
        self.dam = [Veneno, Tierra, Roca, Fantasma]
        self.recibed = [Tierra, Psiquico]
        self.recibem = [Pelea, Veneno, Bicho, Planta, Hada]
        self.dad = [Planta, Hada]
        self.da0 = [Acero]


class Tierra(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Tierra"
        self.dam = [Bicho, Planta]
        self.recibed = [Agua, Planta, Hielo]
        self.recibem = [Veneno, Roca]
        self.dad = [Veneno, Roca, Acero, Fuego, Electrico]
        self.da0 = [Volador]
        self.recibe0 = [Electrico]


class Roca(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Roca"
        self.dam = [Pelea, Tierra, Acero]
        self.recibed = [Pelea, Tierra, Acero, Agua, Planta]
        self.recibem = [Normal, Volador, Veneno, Fuego]
        self.dad = [Volador, Bicho, Fuego, Hielo]


class Bicho(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Bicho"
        self.dam = [Pelea, Volador, Veneno, Fantasma, Acero, Fuego, Hada]
        self.recibed = [Volador, Roca, Fuego]
        self.recibem = [Pelea, Tierra, Planta]
        self.dad = [Planta, Psiquico, Siniestro]


class Fantasma(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Fantasma"
        self.dam = [Siniestro]
        self.recibed = [Fantasma, Siniestro]
        self.recibem = [Veneno, Bicho]
        self.dad = [Fantasma, Psiquico]
        self.da0 = [Normal]
        self.recibe0 = [Normal, Pelea]


class Acero(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Acero"
        self.dam = [Acero, Fuego, Agua, Electrico]
        self.recibed = [Pelea, Tierra, Fuego]
        self.recibem = [Normal, Volador, Roca, Bicho, Acero, Planta, Psiquico, Hielo, Dragon, Hada]
        self.dad = [Roca, Hielo, Hada]
        self.recibe0 = [Veneno]


class Fuego(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Fuego"
        self.dam = [Roca, Fuego, Agua, Dragon]
        self.recibed = [Tierra, Roca, Agua]
        self.recibem = [Bicho, Acero, Fuego, Planta, Hielo, Hada]
        self.dad = [Bicho, Acero, Planta, Hielo]


class Agua(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Agua"
        self.dam = [Agua, Planta, Dragon]
        self.recibed = [Planta, Electrico]
        self.recibem = [Acero, Fuego, Agua, Hielo]
        self.dad = [Tierra, Roca, Fuego]


class Planta(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Planta"
        self.dam = [Volador, Veneno, Bicho, Acero, Fuego, Planta, Dragon]
        self.recibed = [Volador, Veneno, Bicho, Fuego, Hielo]
        self.recibem = [Tierra, Agua, Planta, Electrico]
        self.dad = [Tierra, Roca, Agua]


class Electrico(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Electrico"
        self.dam = [Planta, Electrico, Dragon]
        self.recibed = [Tierra]
        self.recibem = [Volador, Acero, Electrico]
        self.dad = [Volador, Agua]
        self.da0 = [Tierra]


class Psiquico(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Psiquico"
        self.dam = [Acero, Psiquico]
        self.recibed = [Bicho, Fantasma, Siniestro]
        self.recibem = [Pelea, Psiquico]
        self.dad = [Pelea, Veneno]
        self.da0 = [Siniestro]


class Hielo(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Hielo"
        self.dam = [Acero, Fuego, Agua, Hielo]
        self.recibed = [Pelea, Roca, Acero, Fuego]
        self.recibem = [Hielo]
        self.dad = [Volador, Tierra, Planta, Dragon]


class Dragon(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Dragon"
        self.dam = [Acero]
        self.recibed = [Hielo, Dragon, Hada]
        self.recibem = [Fuego, Agua, Planta, Electrico]
        self.dad = [Dragon]
        self.da0 = [Hada]


class Siniestro(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Siniestro"
        self.dam = [Pelea, Siniestro, Hada]
        self.recibed = [Pelea, Bicho, Hada]
        self.recibem = [Fantasma, Siniestro]
        self.dad = [Fantasma, Psiquico]
        self.recibe0 = [Psiquico]


class Hada(Tipo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = "Hada"
        self.dam = [Veneno, Acero, Fuego]
        self.recibed = [Veneno, Acero]
        self.recibem = [Pelea, Bicho, Siniestro]
        self.dad = [Pelea, Dragon, Siniestro]
        self.recibe0 = [Dragon]


class Doble(Tipo):
    def __init__(self, primera, segunda):
        super().__init__()
        p = primera()
        s = segunda()
        self.nombre = p.nombre + "-" + s.nombre
        self.dam = p.dam + s.dam
        self.recibed = p.recibed + s.recibed
        self.recibem = p.recibem + s.recibem
        self.dad = p.dad + s.dad
        self.da0 = p.da0 + s.da0
        self.recibe0 = p.recibe0 + s.recibe0


ta = Doble(Tierra, Agua)

