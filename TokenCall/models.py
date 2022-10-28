from django.db import models
    
class TokenTable(models.Model):
    
    Tokens = models.CharField(max_length=100)
    CustomerName = models.CharField(max_length=100)
    CallStatus = models.BooleanField(default=False)
    Token_date =models.DateTimeField(auto_now_add=True)
    
