import psycopg2

def create_db(cursor):
    cursor.execute("""
    create table if not exists client_table(
        client_id integer not null primary key,
        first_name char(30) not null,
        last_name char(30) not null,   
        email char(30) not null     
    );
    """)
    cursor.execute("""
    create table if not exists phone_table(
        p_id integer  not null primary key,
        phone char(30) not null,
        client_id_ integer not null references client_table(client_id) 
    );
    """)  
    conn.commit() 
    print("База данных создана!")
    return

def delete_db(cursor):
    cursor.execute("""
    drop table phone_table;
    """)
    cursor.execute("""
    drop table client_table;
    """)
    conn.commit()
    print("База данных удалена!")
    return 

def add_client(cursor, client_id_,first_name_, last_name_, email_):
    cursor.execute("""
    insert into client_table(client_id,first_name,last_name,email)
    values
        (%s, %s, %s, %s);
    """,(client_id_, first_name_, last_name_, email_,))  
    conn.commit()
    print(f'Клиент {first_name_} {last_name_} создан!')
    return

def add_phone(cursor,p_id_,phone_,client_id_):
    cursor.execute("""
    INSERT INTO phone_table(p_id,phone,client_id)
        VALUES
        (%s, %s, %s, %s);
    """,(p_id_, phone_, client_id_,))  
    conn.commit()
    print(f'телефон {phone_} добавлен!')
    return 

def change_client(cursor, client_id_, first_name_, last_name_, email_):
   cursor.execute(""" 
    update  client_table 
    set  first_name = %s,
         last_name = %s,  
         email = %s,   
    where client_id = %s;
    """,(first_name_, last_name_, email_,client_id_,))
    conn.commit()
    print(f'Данные клиента {client_id_} изменены')
    return

def delete_phone(cursor, phone_):
    cursor.execute("""
    DELETE FROM phone_table WHERE phone=%s;
    """, (phone_,))
    conn.commit()
    print(f'телефон {phone_} удален')
    return

def delete_client(cursor, client_id_):   
    cursor.execute("""
    DELETE FROM client_table WHERE client_id=%s;
    """, (client_id_,))
    conn.commit()
    print(f'Клиент {client_id} удален')
    return

def find_client(cursor, client_id_):
    cursor.execute("""
    SELECT FROM client_table WHERE client_id=%s;
    """, (client_id_,))
    conn.commit()
    print(f'Клиент {client_id} найден')
    return

with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        n = 1
        while (n < 9) and (n > 0):
            print ("Создать БД: 1 ; Удалить БД: 2 ; Добавить клиента: 3 ; Удалить клиента: 4 ; Добавить телефон: 5 ; Удалить телефон: 6 ")
            print ("Найти клиента: 7 ; Изменить данные клиента: 8; Выход из программы 0")
            n = int(input ("Введите код операции  (от 0 до 8) -> "))
            if n == 0:
                print("Работа программы завершена")        
            if n == 1:
                create_db(cur)                
            if n == 2:
                delete_db(cur)                  
            if n == 3:
                client_id_ = input("Введите ID клиента -> ")
                first_name_ = input("Введите имя клиента -> ")
                last_name_ = input("Введите фамилию клиента -> ")
                email_ = input ("Введите эл. почту клиента -> ")
                p_id_  = input ("Ведите ID телефона клиента -> ")
                phone_ = input ("Ведите телефон клиента -> ")
                add_client(cur,client_id_,first_name_,last_name_,email_)
                add_phone(cur,p_id_,phone_,client_id_)
            
            if n == 4:
                client_id_ = input("Введите ID клиента -> ")
                delete_client(cur, client_id_)
            
            if n == 5:
                p_id_ = input("Введите ID телефона -> ")
                phone_ = input ("Введите телефон клиента -> ")
                client_id_ = input("Введите ID клиента -> ")
                add_phone(cur,p_id_,phone_,client_id_)
            
            if n == 6:
                phone_ = input ("Введите телефон клиента -> ") 
                delete_phone(cur, phone_)
            
            if n == 7:
                client_id_ = input("Введите ID клиента -> ")
                find_client(cur,client_id_)
            
            if n == 8:
                client_id_ = input("Введите ID клиента -> ")
                first_name_ = input("Введите имя клиента -> ")
                last_name_ = input("Введите фамилию клиента -> ")
                email_ = input ("Введите эл. почту клиента -> ")
                change_client(cur,client_id_,first_name_,last_name_,email_)
            
conn.close()
        