import hashlib
import generators

# check user availability
check_user = "Select user_id from Maarifa_Users where address = {address}"

# user registration
user_register = "Insert into Maarifa_Users (username, address, number, authentication_string, date_created, last_updated)" " values()"

# user login sql statements
user_login_1 = "Select authentication_string from Maarifa_Users where address = {address}"
user_login_2 = "Select SHA2('" + hashlib.sha3_512(eval("b'{password}'")).hexdigest() + "', 256)"
user_login_3 = "Update Maarifa_Users set last_updated = '" + generators.cur_day_generator() + "' where address = {address}"

# user profile statements
user_profile_1 = "Select first_name, last_name, address, phone_number from Maarifa_Users where user_id = {user_id}"
user_profile_2 = "Update Maarifa_Users set first_name = {f_name}, last_name = {l_name}, email = {email}, phone_number = {number} where user_id = {user_id}"
user_profile_3 = "Select authentication_string from Maarifa_Users where user_id = {user_id}"
user_profile_4 = "Update Maarifa_Users set authentication_string = {p_word} where user_id = {user_id}"
