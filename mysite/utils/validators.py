from rest_framework.exceptions import ValidationError

def validate_password(password):
    if password is None:
        raise ValidationError({"msg":"密码不能为空"})
    if len(password) < 6:
        raise ValidationError({"msg":"密码长度不能少于6个字符"})
    if " " in password:
        raise ValidationError({"msg":"密码不能包含空格"})
    return password