from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == '\'or1=1':
        raise ValidationError("Content is similar to Sql injection")

    if content.strip() == '':
        raise ValidationError("Content can not be blank or space only!")

    return value