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
        return generators.execute_sql(sql_stmt.admin_profile_4.format(password=old_password), result_flag=True)[0]
    return False
