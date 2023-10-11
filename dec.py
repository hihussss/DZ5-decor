from datetime import datetime

def logger(old_function):
    
    def new_function(*args, **kwargs):
        time = datetime.now()
        file_content = ("{}-{}-{}-{}-{}\n").format(time,old_function.__name__,args,kwargs,old_function(*args, **kwargs))
        with open('main.log', 'a', encoding='utf8') as f:
                f.write(file_content)
        result = old_function(*args, **kwargs)
        
        return result

    return new_function

# def logger(path):
    
#         def __logger(old_function):
#             def new_function(*args, **kwargs):
#                 time = datetime.now()
#                 file_content = ("{}-{}-{}-{}-{}\n").format(time,old_function.__name__,args,kwargs,old_function(*args, **kwargs))
#                 with open(path, 'a', encoding='utf8') as f:
#                     f.write(file_content)
#                 result = old_function(*args, **kwargs)
#                 return result

#             return new_function

#         return __logger