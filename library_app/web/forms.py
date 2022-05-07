from django import forms

from library_app.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }


# class DeleteBookForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for _, field in self.fields.items():
#             field.widget.attrs['readonly'] = 'readonly'
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#         labels = {
#             'title': 'Title',
#             'description': 'Description',
#             'image': 'Image',
#             'type': 'Type',
#         }