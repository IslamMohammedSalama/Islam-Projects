# '''this module is only print hello in terminal'''
# def say_hello(name) -> str:

#     '''this module is only print hello in terminal'''
    
#     mg = 'hello'
#     return f"{mg} {name}"
    
# print(say_hello('Islam'))

import sqlite3

ls  = ['ahmed', 'osama' ,'islam','hashem','sayed','mohamead']

conn = sqlite3.connect('skills.db')
cr = conn.cursor()
# cr.execute('create table if not exists users(number intger , user text)')
cr.execute('select * from users ')
# cr.execute(f"insert into users(number, users) values({ls.index('ahmed')},'{ls[3]}')")
cr.execute('update users set user = "islam" where number= 1')
cr.execute('insert into users values(2, "islam")')
# cr.execute('delete from users where number=2')


# print(cr.fetchall())
# conn.commit()

conn.close()
print('all added')

