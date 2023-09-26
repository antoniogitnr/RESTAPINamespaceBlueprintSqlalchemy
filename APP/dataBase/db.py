from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('mysql+pymysql://panda:root@localhost/poo')
Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)

Base.metadata.create_all(engine)

def crear_sesion(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def all():
    session = crear_sesion(engine)
    productos = session.query(Producto)
    result = []
    for product in productos:
        tuplaproducto = (product.id,product.name,product.price,product.quantity)
        result.append(tuplaproducto)
    return result

def one(idproducto):
    session = crear_sesion(engine)
    producto =session.query(Producto).filter_by(id=idproducto).first()
    if producto:
        print(producto.id,producto.name,producto.price,producto.quantity)
        returnproduct = (producto.id,producto.name,producto.price,producto.quantity)
        return returnproduct
    

def addProducto(tuplaproducto):
    session = crear_sesion(engine)
    name,price,quantity = tuplaproducto
    new_producto = Producto(name=name,price=price,quantity=quantity) 
    session.add(new_producto)
    session.commit() 
    print('producto agregado')
    session.close() 

def deleteProducto(idproducto):
    session = crear_sesion(engine)
    producto = session.query(Producto).filter_by(id=idproducto).first()
    if producto:     
            session.delete(producto)
            session.commit() 
            session.close()
            return 'Producto eliminado'
    else:
        session.close()
        return 'no se encontro producto'
     

def updateProducto(id,modificar):
    session = crear_sesion(engine)
    productoactu = session.query(Producto).filter_by(id=id).first()
    if productoactu:
        productoactu.name = modificar[0]
        productoactu.price = modificar[1]
        productoactu.quantity = modificar[2]
        session.commit()
        session.close()
        return ('Producto actualizado')
    else:
        return ('Producto no encontrado')
        

if __name__ == '__main__':
    """ srg = 25
    tupla = ('chaooooo', 0, 0)
    updateProducto(srg,tupla) """