from .models import Client

def create_customer_user(user):
    """
    Regra de negócio pura: Todo novo usuário via site 
    é um cliente e ganha um perfil automático.
    """
    user.is_client = True
    user.is_barber = False
    user.save()
    Client.objects.get_or_create(user=user)