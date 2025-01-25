from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    identification = models.CharField(max_length=20, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'



class Account(models.Model):
    ACCOUNT_TYPE = [
        ('corriente', 'Corriente'),
        ('ahorro', 'Ahorro')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=10, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    funds = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.username} - {self.account_number} - {self.account_type}"

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSITO', 'Depósito'),
        ('RETIRO', 'Retiro'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('PAGO SERVICIOS BASICOS', 'Pago de servicios básicos')
    ]
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.timestamp}"

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'

class Service(models.Model):
    SERVICE_TYPES = [
        ('AGUA', 'Factura de agua'),
        ('ELECTRICIDAD', 'Factura de Luz'),
    ]
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    bill_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.service_type} payment - {self.bill_number}"

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'