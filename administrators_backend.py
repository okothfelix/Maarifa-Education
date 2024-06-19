import generators
import sql_stmt


def admin_login(username, password):
    try:
        result_set = generators.execute_sql(sql_stmt.admin_login_1.format(address=username), result_flag=True)[1][0]
    except Exception:
        return False
    p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=password), result_flag=True)[1][0]
    if p_word == result_set[1][0]:
        sub_set = generators.execute_sql(sql_stmt.admin_login_3.format(address=username), commit_flag=True)
        return sub_set[0]
    return False


def admin_dashboard():
    pass


def add_lower_learning(created_by, first_name, last_name, email, phone_number, institution_name, username, location):
    cur_day = generators.cur_day_generator()
    try:
        generators.execute_sql(sql_stmt.add_lower_learning.format(created_by=created_by, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, institution_name=institution_name, username=username, location=location, date_created=cur_day, last_updated=cur_day), commit_flag=True)
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1146":
            generators.execute_sql(sql_stmt.add_lower_learning_1, commit_flag=True)
        if str(e)[:str(e).find(" ")] == "1062":
            return False
        else:
            print(e)
            return


def add_admin(created_by, first_name, last_name, email, phone_number, create_flag,):
    try:
        cur_day = generators.cur_day_generator()
        generators.execute_sql(sql_stmt.add_administrators.format(create_by=created_by, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, date_created=cur_day, last_updated=cur_day), commit_flag=True)
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1062":
            pass
        else:
            print(e)
            return


def view_administrators():
    return generators.execute_sql(sql_stmt.view_administrators())

 
def admin_profile_section(method, user_id=0, f_name="", l_name="", email="", number=""):
    if method == 'POST':
        return generators.execute_sql(sql_stmt.admin_profile_2.format(f_name=f_name, l_name=l_name, email=email, number=number, user_id=user_id), result_flag=False, commit_flag=True)[0]
    else:
        return generators.execute_sql(sql_stmt.admin_profile_1.format(user_id=user_id), result_flag=True)


def update_admin_password_section(admin_id, old_password, new_password):
    user_password = generators.execute_sql(sql_stmt.admin_profile_3.format(admin_id=admin_id), result_flag=True)[1][0]
    p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=old_password), result_flag=True)[1][0]
    if user_password == p_word:
        p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=new_password), result_flag=True)[1][0]
        return generators.execute_sql(sql_stmt.admin_profile_4.format(p_word=p_word), result_flag=True)[0]
    return False
