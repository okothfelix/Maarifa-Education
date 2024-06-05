import generators
import sql_stmt


def user_login(username, password):
    try:
        result_set = generators.execute_sql(sql_stmt.user_login_1.format(address=username), result_flag=True)[1][0][0]
    except Exception:
        return False
    p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=password), result_flag=True)[1][0][0]
    if p_word == result_set:
        sub_set = generators.execute_sql(sql_stmt.user_login_3.format(address=username), commit_flag=True)
        return sub_set[0]
    return False


def user_profile_section(method, user_id=0, f_name="", l_name="", email="", number=""):
    if method == 'POST':
        generators.execute_sql(sql_stmt.user_profile_2.format(f_name=f_name, l_name=l_name, email=email, number=number, user_id=user_id), commit_flag=True)
    else:
        return generators.execute_sql(sql_stmt.user_profile_1.format(user_id=user_id), result_flag=True)[1][0]


def update_user_password_section(user_id, old_password, new_password):
    user_password = generators.execute_sql(sql_stmt.user_profile_3.format(user_id=user_id), result_flag=True)[1][0][0]
    p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=old_password), result_flag=True)[1][0][0]
    if user_password == p_word:
        p_word = generators.execute_sql(sql_stmt.user_login_2.format(password=new_password), result_flag=True)[1][0][0]
        return generators.execute_sql(sql_stmt.user_profile_4.format(p_word=p_word, user_id=user_id), commit_flag=True)[0]
    return False
