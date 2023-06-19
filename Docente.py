

from Persona import Persona

class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, carrera, titulo_3er_nivel, titulo_4to_nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, carrera)
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, nuevo_titulo):
        self._titulo_3er_nivel = nuevo_titulo

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, nuevo_titulo):
        self._titulo_4to_nivel = nuevo_titulo

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True

    def __str__(self):
        return f"Docente: {self.nombre} {self.apellido}, Carrera: {self.carrera}, Título 3er Nivel: {self.titulo_3er_nivel}, Título 4to Nivel: {self.titulo_4to_nivel}"

if __name__ == "__main__":
    docente = Docente("987654321", "Livington", "Gallardo", "livi@example.com", "0987654321", "Avenida Principal", "Ingeniería", "Ph.D.", "M.Sc.")
    print(docente)
