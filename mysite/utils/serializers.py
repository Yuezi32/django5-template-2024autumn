# 用于将serializer.errors转化为适合API msg显示的字符串。
def stringifySerializereErrors(obj):
    """
    obj = serializer.errors
    """
    errors_str = ", ".join(
        f"{field}:{'; '.join(map(str, errors))}" for field, errors in obj.items()
    )
    return errors_str