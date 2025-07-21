def check_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("is_admin", False):
            return func(*args, **kwargs)
        else:
            print("Доступ запрещён. Только для админов.")
    return wrapper

@check_admin
def delete_user(*args, **kwargs):
    print("Пользователь удалён.")

@check_admin
def delete_post(*args, **kwargs):
    print("Пост удалён.")

delete_user(is_admin=True)
delete_post(is_admin=False)
