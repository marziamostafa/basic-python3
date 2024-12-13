def full_name(f_name,l_name):
    name=f'{f_name} {l_name}'
    return name
name=full_name(l_name='Mostafa',f_name='Marzia')
print(name)

# kargs
def long_name(**kargs):
    print(kargs)
long_name(first='Marzia',middle='mostafa',last='moon')

def mixed_name(first,last,**kargs):
    print(first,last,kargs)
mixed_name(first='Marzia',middle='mostafa',last='moon')


def all_type(first,*args,**kargs):
    print(first,args,kargs)
    for key, value in kargs.items():
        print(key,value)


all_type('aaa','bbb','ccc','ddd',name='marzia',middle='mostafa')