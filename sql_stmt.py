import hashlib
import generators

# user pilot registration statements
user_pilot_register_1 = "Insert into Maarifa_Pilots (username, institution_name, level, address, phone_number, date_created) values ({username}, {institution_name}, {level}, {email}, {number}, {date_created})"
user_pilot_register_2 = "Create table Maarifa_Pilots (pilot_id int not null primary key auto_increment, username varchar(30) not null, institution_name varchar(50) not null, address varchar(50) not null default '', phone_number varchar(20) not null, status tinyint not null default 0, date_created timestamp not null)"

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


# lower_learning statements start here

# add a lower learning institution
add_lower_learning = "Insert into Maarifa_Lower_Learning_Institutions (created_by, first_name, last_name, email, phone_number, institution_name, username, location, date_created, last_updated) values({created_by}, {first_name}, {last_name}, {email}, {phone_number}, {date_created}, {last_updated})"
add_lower_learning_1 = "Create table Maarifa_Lower_Learning_Institution (institution_id int not null primary key auto_increment, created_by int not null, first_name varchar(30) not null, last_name varchar(30) not null, email varchar(50) not null, phone_number varchar(20) not null, authentication_string varchar(64) not null default '', status tinyint not null default 0, date_created timestamp not null, last_updated timestamp not null)"

# adding a lower instructor administrator
lower_instructor_administrator = "Select admin_id from Maarifa_Lower_Learning_Administrators where "
lower_instructor_administrator_1 = "Create table Maarifa_Lower_Learning_Administrators (admin_id int not null primary key auto_increment, created_by in not null, first_name varchar(30) not null, last_name varchar(30) not null, email varchar(50) not null default '', )"

# adding a lower learning instructor
lower_learning_instructor = "Select instructor_id from Maarifa_Lower_Learning_Instructors where phone_number = {phone_number}"
lower_learning_instructor_1 = "Create table Maarifa_Lower_Learning_Instructors (instructor_id int not null primary key auto_increment, created_by int not null, )"

# lower_learning available sms
lower_sms = "Select available_sms from Maarifa_Lower_Learning where i_d = {id}"
lower_sms_update = "Update Maarifa_Lower_Learning set available_sms = {available_sms} where i_d = {id}"


# admin login statements
admin_login_1 = "Select authentication_string from Maarifa_Administrators where address = {address}"
admin_login_2 = "Select SHA2('" + hashlib.sha3_512(eval("b'{password}'")).hexdigest() + "', 256)"
admin_login_3 = "Update Maarifa_Administrators set last_updated = '" + generators.cur_day_generator() + "' where address = {address}"

# admin profile statements
admin_profile_1 = "Select first_name, last_name, address, phone_number from Maarifa_Administrators where admin_id = {user_id}"
admin_profile_2 = "Update Maarifa_Administrators set first_name = {f_name}, last_name = {l_name}, email = {email}, phone_number = {number} where admin_id = {user_id}"
admin_profile_3 = "Select authentication_string from Maarifa_Administrators where user_id = {user_id}"
admin_profile_4 = "Update Maarifa_Administrators set authentication_string = {p_word} where admin_id = {user_id}"

# admin available sms
admin_sms = "Select available_sms from Maarifa_Administrators"
