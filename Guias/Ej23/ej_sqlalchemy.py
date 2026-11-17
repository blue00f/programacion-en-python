from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

def ejecutar():
    print("\n--- 7. SQLALCHEMY ---")
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    nuevo_usuario = Usuario(nombre="Carlos")
    session.add(nuevo_usuario)
    session.commit()
    
    usuario = session.query(Usuario).first()
    print(f"Usuario recuperado desde BD en memoria: {usuario.nombre}")
    session.close()