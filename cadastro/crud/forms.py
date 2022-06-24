from attr import fields
from django import forms

from cadastro.crud.models import Cliente

class Clientform(forms.ModelForm):
  
  class Meta:
    model=Cliente
    fields=('fullnome','endereco','produto')
    labels={'fullnome':'Nome Completo','endereco':'Endereco'}

    def __init__(self,*args,**kwargs) -> None:  
      super(Clientform,self).__init__(*args,**kwargs)
      self.fields['produto'].empty_label="Select"
      self.fields['endereco'].required=False

