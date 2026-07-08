from .models import Producto


class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session

        carrito = self.session.get("carrito")

        if not carrito:
            carrito = self.session["carrito"] = {}

        self.carrito = carrito

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def agregar(self, producto):

        producto_id = str(producto.id)

        if producto_id not in self.carrito:

            self.carrito[producto_id] = {
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
            }

            self.guardar()

            return True

        if self.carrito[producto_id]["cantidad"] < producto.stock:

            self.carrito[producto_id]["cantidad"] += 1

            self.guardar()

            return True

        return False

    def eliminar(self, producto):

        producto_id = str(producto.id)

        if producto_id in self.carrito:

            del self.carrito[producto_id]

            self.guardar()

    def restar(self, producto):

        producto_id = str(producto.id)

        if producto_id in self.carrito:

            self.carrito[producto_id]["cantidad"] -= 1

            if self.carrito[producto_id]["cantidad"] <= 0:

                self.eliminar(producto)

            else:

                self.guardar()

    def limpiar(self):

        self.session["carrito"] = {}

        self.session.modified = True
    
    def vaciar(self):

        self.session["carrito"] = {}

        self.carrito = self.session["carrito"]

        self.session.modified = True
