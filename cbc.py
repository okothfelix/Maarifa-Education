import generators
import sql_stmt


def user_login(username, password):
    conn = generators.connect_to_mysql()
    c = conn.cursor(buffered=True)
    try:
        c.execute(sql_stmt.user_login_1.format(address=username))
        result_set = c.fetchone()[0]
    except TypeError:
        conn.close()
        return False
    except Exception as e:
        conn.close()
        if str(e)[:str(e).find(" ")] == "1146":
            return False
        else:
            print(e)
            conn.close()
            return False
    c.execute(sql_stmt.user_login_2.format(password=password))
    p_word = c.fetchone()[0]
    if p_word == result_set:
        c.execute(sql_stmt.user_login_3.format(address=username))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False


def user_dashboard(user_id):
    _dashboard = []
    conn = generators.connect_to_mysql()
    c = conn.cursor(buffered=True)
    conn.close()
    return _dashboard


def user_profile_section(method, user_id=0, f_name="", l_name="", email="", number=""):
    conn = generators.connect_to_mysql()
    c = conn.cursor(buffered=True)
    if method == "POST":
        c.execute(sql_stmt.user_profile_2.format(f_name=f_name, l_name=l_name, email=email, number=number, user_id=user_id))
        conn.commit()
        conn.close()
    else:
        # get the users details
        c.execute(sql_stmt.user_profile_1.format(user_id=user_id))
        result_set = c.fetchone()
        conn.close()
        return result_set


def update_admin_password_section(user_id, old_password, new_password):
    conn = generators.connect_to_mysql()
    c = conn.cursor(buffered=True)
    c.execute(sql_stmt.user_profile_3.format(user_id=user_id))
    previous_pass = c.fetchone()[0]
    c.execute(sql_stmt.user_login_2.format(password=old_password))
    p_word = c.fetchone()[0]
    if previous_pass == p_word:
        c.execute(sql_stmt.user_login_2.format(password=new_password))
        p_word = c.fetchone()[0]
        c.execute(sql_stmt.user_profile_4.format(p_word=p_word, user_id=user_id))
        conn.commit()
        conn.close()
        return True
    return False
