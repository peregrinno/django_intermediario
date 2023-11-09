from django import forms
from django.core.mail.message import EmailMessage

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario

class CustonUsuarioCreateForm(UserCreationForm):
    
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username':'Username/E-mail'}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        
        
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    numero = forms.IntegerField(label='Numero')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome =  self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        numero = self.cleaned_data['numero']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f' Nome: {nome}\n Email: {email}\n Assunto: {assunto}\n Numero: {numero}\n Mensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@andromeda.com.br',
            to=['contato@andromeda.com.br',],
            headers={'Reply-To': email}
        )

        mail.send()