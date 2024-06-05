import hashlib
import generators

# user registration statements
user_register_1 = "Select user_id from Maarifa_Users where address = {address}"
user_register_2 = "Insert into Maarifa_Users (username, address, phone_number, authentication_string, date_created, last_updated) values ({username}, {email}, {number}, {password}, {date_created}, {last_updated})"
user_register_3 = "Create table Maarifa_Users (user_id int not null primary key auto_increment, username varchar(30) not null, address varchar(50) not null, phone_number varchar(20) not null, status tinyint not null default 0, date_created timestamp not null, last_updated timestamp not null, unique key users (address))"

# user account activation statement
activation_1 = "Select activation_code from Account_Activation where activation_code = {activation_code}"
activation_2 = "Create table Account_Activation (activation_id int not null primary key auto_increment, user_type tinyint not null default 0, activation_code varchar(20) not null, address varchar(50) not null default '', date_added timestamp not null, unique key codes (activation_code))"
activation_3 = "Insert into Account_Activation (user_type, activation_code, address, date_added) values ({user_type}, {activation_code}, {address}, {date_added})"

# user login statements
user_login_1 = "Select authentication_string from Maarifa_Users where address = {address}"
user_login_2 = "Select SHA2('" + hashlib.sha3_512(eval("b'{password}'")).hexdigest() + "', 256)"
user_login_3 = "Update Maarifa_Users set last_updated = '" + generators.cur_day_generator() + "' where address = {address}"

# user profile statements
user_profile_1 = "Select first_name, last_name, address, phone_number from Maarifa_Users where user_id = {user_id}"
user_profile_2 = "Update Maarifa_Users set first_name = {f_name}, last_name = {l_name}, email = {email}, phone_number = {number} where user_id = {user_id}"
user_profile_3 = "Select authentication_string from Maarifa_Users where user_id = {user_id}"
user_profile_4 = "Update Maarifa_Users set authentication_string = {p_word} where user_id = {user_id}"

# admin login statements
admin_login_1 = "Select authentication_string from Maarifa_Administrators where address = {address}"
admin_login_2 = "Select SHA2('" + hashlib.sha3_512(eval("b'{password}'")).hexdigest() + "', 256)"
admin_login_3 = "Update Maarifa_Administrators set last_updated = '" + generators.cur_day_generator() + "' where address = {address}"

# admin profile statements
admin_profile_1 = "Select first_name, last_name, address, phone_number from Maarifa_Administrators where admin_id = {user_id}"
admin_profile_2 = "Update Maarifa_Administrators set first_name = {f_name}, last_name = {l_name}, email = {email}, phone_number = {number} where admin_id = {user_id}"
admin_profile_3 = "Select authentication_string from Maarifa_Administrators where user_id = {user_id}"
admin_profile_4 = "Update Maarifa_Administrators set authentication_string = {p_word} where admin_id = {user_id}"