from sqlalchemy import create_engine, delete, Table, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base




engine = create_engine('sqlite:///database/visitors_sq.db')

Base = declarative_base()

class Visitor(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True)
    last_name = Column(String(20))
    first_name = Column(String(20))
    pin = Column(String(4), nullable=False, unique=True)
    status = Column(Integer, nullable=False)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


#region initial visitors
# Visitors = [
#     Visitor(last_name='', first_name='admin', pin='0000', status='1'),
#     Visitor(last_name='Peric', first_name='Pero', pin='1234', status='1'),
#     Visitor(last_name='Maric', first_name='Marko', pin='2345', status='1'),
#     Visitor(last_name='Anic', first_name='Ana', pin='3456', status='1'),
#     Visitor(last_name='Ivic', first_name='Iva', pin='4567', status='1')
# ]

# for visitor in Visitors:
#     session.add(visitor)
# session.commit()
#endregion


def add_update_visitor(db_entry_first_name, db_entry_last_name, db_entry_pin, db_entry_status):
    
    try:
        existing_row = session.query(Visitor).filter_by(first_name=db_entry_first_name).first()
        
        return_msg = ''

        if session.query(Visitor).filter_by(pin=db_entry_pin).first():
             return 'Pin se već koristi.\nMolim unesite drugi pin!'

        if existing_row:
            existing_row.first_name = db_entry_first_name
            existing_row.last_name = db_entry_last_name
            existing_row.pin = db_entry_pin
            existing_row.status = db_entry_status
            return_msg = 'Uspjepšno ste ažurirali podatke!'
        
        else:
            visitor_obj = Visitor(first_name=db_entry_first_name,
                                last_name=db_entry_last_name,
                                pin=db_entry_pin,
                                status=db_entry_status)
            session.add(visitor_obj)
            return_msg = 'Uspjepšno ste dodali \novlastili posjetitelja!'

        session.commit()
        
    except Exception as ex:
        session.rollback()
        return_msg = f'Došlo je do pogreške prilikom unosa!\n{ex}'
    
    finally:
         session.close()

    return return_msg



def check_pin(entered_pin):
    visitor_from_db = session.query(Visitor).filter_by(pin=entered_pin).first()
    if visitor_from_db != None:
        if visitor_from_db.pin == entered_pin and visitor_from_db.status == 1:
            return True
    else:
        return False


def get_visitor_info(entered_pin):
            return session.query(Visitor).filter_by(pin=entered_pin).first()
    

def get_visitor(user_first_name):
            return session.query(Visitor).filter_by(first_name=user_first_name).first()


def get_visitors():
     visitors_from_db = session.query(Visitor).all()
     visitors_names = []
     for visitor in visitors_from_db:
          visitor_var = visitor.first_name + ' ' + visitor.last_name
          visitors_names.append(visitor_var)
     return visitors_names
     

def del_visitor(first_name):

    visitor_obj = session.query(Visitor).filter_by(first_name=first_name).first()
    return_msg = ''
    del_obj = visitor_obj.first_name

    try:
        row_to_delete = get_visitor(del_obj)
        if row_to_delete:
            session.delete(row_to_delete)
            session.commit()
            return_msg = 'Uspješno ste obrisali posjetitelja.'
        else:
            return_msg = 'Posjetitelj nije pronađen.'
    except Exception as e:
        session.rollback()
        return_msg = 'Greška pri brisanju posjetitelja.'
    finally:
        session.close()
    
    return return_msg
      

