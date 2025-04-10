from django import forms

class ColorInput(forms.TextInput):
    input_type = 'color'

class GetUrlForm(forms.Form):
    url = forms.CharField(label='URL', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Enter URL'}))
    fill_color = forms.CharField(label='Fill Color', max_length=7, widget=ColorInput(attrs={'placeholder': 'Enter Color'}))
    background_color = forms.CharField(label='Background Color', max_length=7, widget=ColorInput(attrs={'placeholder': 'Enter Color', 'value': '#ffffff'}))
    # embedded_image = forms.ImageField(label='Embedded Image', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    # rounded = forms.BooleanField( 
    #     required=False, 
    #     label='Rounded Corners',
    #     help_text='Check to apply rounded corners to the QR code.',
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',  # Bootstrap class (optional)
    #     }))
    # circle = forms.BooleanField( 
    #     required=False, 
    #     label='Circle QR Code',
    #     help_text='Check to apply circle shape to the QR code.',
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',  # Bootstrap class (optional)
    #     })
    # )