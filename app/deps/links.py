

def get_link_depend(obj):
    def func():
        return obj()

    return func
