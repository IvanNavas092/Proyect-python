from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre, edad, id_empleado):
        self.nombre = nombre
        self.edad = edad
        self.id_empleado = id_empleado

    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, ID: {self.id_empleado}"

# Clase Asalariado --> Empleado
class Asalariado(Empleado):
    def __init__(self, nombre, edad, id_empleado, salario_mensual):
        super().__init__(nombre, edad, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

    def __str__(self):
        return f"Empleado Asalariado - {super().__str__()}, Salario Mensual: {self.salario_mensual}"

# Clase Temporal --> Empleado
class Temporal(Empleado):
    def __init__(self, nombre, edad, id_empleado, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, edad, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

    def __str__(self):
        return f"Empleado Temporal - {super().__str__()}, Horas trabajadas: {self.horas_trabajadas}, Pago por hora: {self.pago_por_hora}"

# Clase Empresa 
class Empresa:
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        print(f"Lista de empleados en {self.nombre_empresa}:")
        for empleado in self.empleados:
            print(empleado)

    def calcular_pago_total(self):
        total = sum(empleado.calcular_salario() for empleado in self.empleados)
        return total



empresa = Empresa("NAVAS S.A")

empleado1 = Asalariado("Claudiu", 12, "A1", 2500)
empleado2 = Temporal("Samuek", 4, "A2", 120, 15)
empleado3 = Temporal("Luismi", 28, "A3", 100, 20)

empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)
empresa.agregar_empleado(empleado3)

print(empleado1)



empresa.listar_empleados()

# Calcular 
total_pagos = empresa.calcular_pago_total()
print(f"\nEl total de pagos a empleados es: {total_pagos}")
    


