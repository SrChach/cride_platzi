"""Djengo model utiities"""

# Django
from djsngo.db import models

class CRideModel(models.Model):
    """Comparte Ride base model
    
    CRideModel acts as an abstract base clas from which every
    other model in the project will inhrerit. This class provides
    every table with the following attributes:
        * created (DateTime): Store the datetime the object was created
        * modified (DateTime): Store the last datetime the object was modified
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on thich the object was created.'
    )

    modified = models.DateTimeField(
        'created at',
        auto_now=True,
        help_text='Date time on thich the object was last modified.'
    )

    class Meta:
        """Meta option"""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

# Clase que hereda de una abstracta
class Student(CRideModel):
    name = models.CharField()

    class Meta(CRideModel.META):
        # Para cambiar algunas cosas, pero mantener las propiedades.
        db_table = 'student_role'


"""
Ejemplo de Proxy

Si queremos hacer cambios a la funcionalidad, sin implementar cambios
en la base de datos, añadimos a META el atributo proxy, que no
crea otra tabla pero permite extender funcionalidad
"""
class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

class MyPerson(Person):
    class Meta:
        proxy = True

    def say_hi(name):
        pass

# Llamando al manager del person original
MyPerson.objects.all()

ricardo = MyPerson.objects.get(pk=1)
ricardo.say_hi('Pablo')

"""
Si llamas a los mismos métodos en el padre, no existen,
por que no está extendida la funcionalidad
"""