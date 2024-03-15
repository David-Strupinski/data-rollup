from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PayType(Base):
    __tablename__ = 'payment_types'

    paytype_id = Column(Integer, primary_key=True)
    paytype_name = Column(String(100))

class Provider(Base):
    __tablename__ = 'providers'

    provider_id = Column(String(20), primary_key=True)
    provider_name = Column(String(100))

class EmployeeType(Base):
    __tablename__ = 'employee_types'

    employee_type_id = Column(Integer, primary_key=True)
    employee_type_name = Column(String(100))

class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    paytype_id = Column(Integer, ForeignKey('payment_types.paytype_id'))
    amount = Column(Float)
    date = Column(Date)
    provider_id = Column(String(20), ForeignKey('providers.provider_id'))
    employee_type_id = Column(Integer, ForeignKey('employee_types.employee_type_id'))

    paytype = relationship('PayType', foreign_keys=[paytype_id])
    provider = relationship('Provider', foreign_keys=[provider_id])
    employee_type = relationship('EmployeeType', foreign_keys=[employee_type_id])
