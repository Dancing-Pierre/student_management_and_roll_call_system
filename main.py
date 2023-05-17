import tkinter as tk
from datetime import date
from tkinter import ttk
import tkinter.messagebox as messagebox
import hashlib
import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='students_db',
    charset='utf8mb4',
)


def md5(text):
    """计算文本的 MD5 散列值"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def register(username, password):
    """注册新用户"""
    with conn.cursor() as cursor:
        password_hash = md5(password)
        cursor.execute('INSERT INTO User (username, password_hash) VALUES (%s, %s)', (username, password_hash))
        conn.commit()
        messagebox.showinfo("注册成功", "注册成功，请使用新用户名和密码登录。")  # 弹出消息框提示用户


def login(username, password):
    """验证用户登录"""
    with conn.cursor() as cursor:
        password_hash = md5(password)
        cursor.execute('SELECT * FROM User WHERE username = %s AND password_hash = %s', (username, password_hash))
        result = cursor.fetchone()
        if result is not None:
            messagebox.showinfo("登录成功", "欢迎回来，{}！".format(username))  # 弹出消息框提示用户
        return result is not None


class LoginRegisterFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 修改背景色
        self.master.configure(bg='#2C3E50')
        self.configure(bg='#2C3E50')

        # 创建用户名和密码的输入框
        self.username_label = tk.Label(self, text="用户名", fg='white', bg='#2C3E50', font=("Helvetica", 14))
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.pack()

        # 创建密码输入框
        self.password_label = tk.Label(self, text="密码", fg='white', bg='#2C3E50', font=("Helvetica", 14))
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 14))
        self.password_entry.pack()

        # 创建登录和注册按钮
        self.button_frame = tk.Frame(self, bg="#2C3E50")  # 新建一个框架，放置两个按钮
        self.button_frame.pack(pady=10)

        self.login_button = tk.Button(self.button_frame, text="登陆", font=("Helvetica", 14), fg='white', bg='#1ABC9C',
                                      command=self.login)
        self.login_button.pack(side="left", padx=10)

        self.register_button = tk.Button(self.button_frame, text="注册", font=("Helvetica", 14), fg='white',
                                         bg='#E74C3C',
                                         command=self.register)
        self.register_button.pack(side="left", padx=10)

        # 创建提示信息的标签
        self.info_label = tk.Label(self, text="", fg='white', bg='#2C3E50', font=("Helvetica", 14))
        self.info_label.pack(pady=20)

    def register(self):
        """处理用户注册"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == '' or password == '':
            messagebox.showwarning("输入为空", "请输入用户名和密码")
        else:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM User WHERE username = %s', username)
            result = cursor.fetchone()
            if result is not None:
                messagebox.showerror("注册失败", "该用户名已存在，请重新输入")
            else:
                register(username, password)
                self.username_entry.delete(0, tk.END)  # 清空用户名输入框
                self.password_entry.delete(0, tk.END)  # 清空密码输入框

    def login(self):
        """处理用户登录"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == '' or password == '':
            messagebox.showwarning("输入为空", "请输入用户名和密码")
        elif login(username, password):
            self.master.destroy()  # 删除登录窗口
            if username == 'admin':
                # 管理员进入用户管理界面
                self.open_admin_window()
            else:
                # 普通用户进入点名界面
                self.open_main_window()
        else:
            messagebox.showerror("登陆失败", "用户名或密码错误")
            self.username_entry.delete(0, tk.END)  # 清空用户名输入框
            self.password_entry.delete(0, tk.END)  # 清空密码输入框

    # 普通用户主页面
    def open_main_window(self):
        # 创建主窗口
        root = tk.Tk()
        root.title("学生管理系统")

        # 创建两个标签页
        self.notebook = ttk.Notebook(root)
        self.notebook.pack()

        # 标签页一：学生信息管理
        self.tab_students = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_students, text="学生信息")

        # 创建学生信息管理界面的控件
        self.frame_students = tk.Frame(self.tab_students)
        self.frame_students.pack(padx=10, pady=10)

        # 创建控件
        self.lb = tk.Listbox(self.frame_students, width=40, height=15)
        self.lb.pack()

        self.frame_add = tk.Frame(self.frame_students)
        self.frame_add.pack(pady=5)

        self.label_id = tk.Label(self.frame_add, text="学号：")
        self.label_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_id = tk.Entry(self.frame_add)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.frame_add, text="姓名：")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.frame_add)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_age = tk.Label(self.frame_add, text="年龄：")
        self.label_age.grid(row=2, column=0, padx=5, pady=5)

        self.entry_age = tk.Entry(self.frame_add)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)

        self.label_gender = tk.Label(self.frame_add, text="性别：")
        self.label_gender.grid(row=3, column=0, padx=5, pady=5)

        self.entry_gender = tk.Entry(self.frame_add)
        self.entry_gender.grid(row=3, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.frame_add, text="电话：")
        self.label_phone.grid(row=4, column=0, padx=5, pady=5)

        self.entry_phone = tk.Entry(self.frame_add)
        self.entry_phone.grid(row=4, column=1, padx=5, pady=5)

        self.btn_add = tk.Button(self.frame_add, text="添加", command=self.add_student)
        self.btn_add.grid(row=5, column=0, padx=5, pady=5)

        self.btn_update = tk.Button(self.frame_add, text="修改", command=self.update_student)
        self.btn_update.grid(row=5, column=1, padx=5, pady=5)

        self.btn_delete = tk.Button(self.frame_add, text="删除", command=self.delete_student)
        self.btn_delete.grid(row=5, column=2, padx=5, pady=5)

        self.frame_search = tk.Frame(self.frame_students)
        self.frame_search.pack(pady=5)

        self.btn_search = tk.Button(self.frame_search, text="搜索", command=self.search_student)
        self.btn_search.grid(row=0, column=2, padx=5, pady=5)

        self.btn_showall = tk.Button(self.frame_search, text="显示全部", command=self.show_students)
        self.btn_showall.grid(row=0, column=3, padx=5, pady=5)

        self.entry_search = tk.Entry(self.frame_search)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        # 显示数据
        self.show_students()

        # 标签页二：点名系统
        self.tab_rollcall = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_rollcall, text="点名系统")

        # 添加当前日期标签
        self.today = date.today().strftime("%Y/%m/%d")
        self.label_date = tk.Label(self.tab_rollcall, text=f"今天是 {self.today}")
        self.label_date.pack(pady=10)

        # 增加点名模式选择器
        self.roll_call_mode = tk.StringVar()
        self.roll_call_mode.set("random")

        self.rb_random = tk.Radiobutton(self.tab_rollcall, text="随机点名", variable=self.roll_call_mode,
                                        value="random",
                                        command=self.set_roll_call_mode_random)
        self.rb_random.pack(pady=10)

        self.rb_sequential = tk.Radiobutton(self.tab_rollcall, text="按顺序点名", variable=self.roll_call_mode,
                                            value="sequential",
                                            command=self.set_roll_call_mode_sequential)
        self.rb_sequential.pack(pady=10)

        # 创建游标对象
        cursor = conn.cursor()
        # 从数据库中检索学生姓名
        query = "SELECT name FROM students"
        cursor.execute(query)
        # 关闭游标和连接
        cursor.close()

        self.btn_roll_call = tk.Button(self.tab_rollcall, text="点名", command=self.roll_call)
        self.btn_roll_call.pack(pady=10)

        # 增加点名结果标签
        self.label_result = tk.Label(self.tab_rollcall, font=("Helvetica", 35), text="")
        self.label_result.pack(pady=10)

        # 增加点名记录按钮
        self.roll_call_history = []

        self.btn_history = tk.Button(self.tab_rollcall, text="查看历史", command=self.view_history)
        self.btn_history.pack(pady=10)

        # 创建点名界面的控件
        self.frame_rollcall = tk.Frame(self.tab_rollcall)
        self.frame_rollcall.pack(padx=10, pady=5)

        self.lb_2 = tk.Listbox(self.frame_rollcall, width=40, height=13)
        self.lb_2.pack()

        # 主循环
        root.mainloop()
        conn.close()

    # 管理用户界面
    def open_admin_window(self):
        # 创建主窗口
        root = tk.Tk()
        root.title("管理员界面")

        # 创建两个标签页
        self.notebook = ttk.Notebook(root)
        self.notebook.pack()

        # 标签页一：用户信息管理
        self.tab_user = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_user, text="管理用户信息")

        # 创建学生信息管理界面的控件
        self.frame_user = tk.Frame(self.tab_user)
        self.frame_user.pack(padx=10, pady=10)

        # 创建控件
        self.lb_user = tk.Listbox(self.frame_user, width=40, height=15)
        self.lb_user.pack()

        self.frame_add = tk.Frame(self.frame_user)
        self.frame_add.pack(pady=5)

        self.label_username = tk.Label(self.frame_add, text="用户名：")
        self.label_username.grid(row=0, column=0, padx=5, pady=5)

        self.entry_username = tk.Entry(self.frame_add)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.label_password = tk.Label(self.frame_add, text="密码：")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_password = tk.Entry(self.frame_add)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.btn_add_user = tk.Button(self.frame_add, text="添加", command=self.add_user)
        self.btn_add_user.grid(row=5, column=0, padx=5, pady=5)

        self.btn_update_user = tk.Button(self.frame_add, text="修改", command=self.update_user)
        self.btn_update_user.grid(row=5, column=1, padx=5, pady=5)

        self.btn_delete_user = tk.Button(self.frame_add, text="删除", command=self.delete_user)
        self.btn_delete_user.grid(row=5, column=2, padx=5, pady=5)

        self.frame_search_user = tk.Frame(self.frame_user)
        self.frame_search_user.pack(pady=5)

        self.btn_search_user = tk.Button(self.frame_search_user, text="搜索", command=self.search_user)
        self.btn_search_user.grid(row=0, column=2, padx=5, pady=5)

        self.btn_showall_user = tk.Button(self.frame_search_user, text="显示全部", command=self.show_user)
        self.btn_showall_user.grid(row=0, column=3, padx=5, pady=5)

        self.entry_search_user = tk.Entry(self.frame_search_user)
        self.entry_search_user.grid(row=0, column=1, padx=5, pady=5)

        # 显示数据
        self.show_user()

        # 标签页一：学生信息管理
        self.tab_students = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_students, text="学生信息")

        # 创建学生信息管理界面的控件
        self.frame_students = tk.Frame(self.tab_students)
        self.frame_students.pack(padx=10, pady=10)

        # 创建控件
        self.lb = tk.Listbox(self.frame_students, width=40, height=15)
        self.lb.pack()

        self.frame_add = tk.Frame(self.frame_students)
        self.frame_add.pack(pady=5)

        self.label_id = tk.Label(self.frame_add, text="学号：")
        self.label_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_id = tk.Entry(self.frame_add)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.frame_add, text="姓名：")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.frame_add)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_age = tk.Label(self.frame_add, text="年龄：")
        self.label_age.grid(row=2, column=0, padx=5, pady=5)

        self.entry_age = tk.Entry(self.frame_add)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)

        self.label_gender = tk.Label(self.frame_add, text="性别：")
        self.label_gender.grid(row=3, column=0, padx=5, pady=5)

        self.entry_gender = tk.Entry(self.frame_add)
        self.entry_gender.grid(row=3, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.frame_add, text="电话：")
        self.label_phone.grid(row=4, column=0, padx=5, pady=5)

        self.entry_phone = tk.Entry(self.frame_add)
        self.entry_phone.grid(row=4, column=1, padx=5, pady=5)

        self.btn_add = tk.Button(self.frame_add, text="添加", command=self.add_student)
        self.btn_add.grid(row=5, column=0, padx=5, pady=5)

        self.btn_update = tk.Button(self.frame_add, text="修改", command=self.update_student)
        self.btn_update.grid(row=5, column=1, padx=5, pady=5)

        self.btn_delete = tk.Button(self.frame_add, text="删除", command=self.delete_student)
        self.btn_delete.grid(row=5, column=2, padx=5, pady=5)

        self.frame_search = tk.Frame(self.frame_students)
        self.frame_search.pack(pady=5)

        self.btn_search = tk.Button(self.frame_search, text="搜索", command=self.search_student)
        self.btn_search.grid(row=0, column=2, padx=5, pady=5)

        self.btn_showall = tk.Button(self.frame_search, text="显示全部", command=self.show_students)
        self.btn_showall.grid(row=0, column=3, padx=5, pady=5)

        self.entry_search = tk.Entry(self.frame_search)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        # 显示数据
        # self.show_students()

        # 标签页二：点名系统
        self.tab_rollcall = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_rollcall, text="点名系统")

        # 添加当前日期标签
        self.today = date.today().strftime("%Y/%m/%d")
        self.label_date = tk.Label(self.tab_rollcall, text=f"今天是 {self.today}")
        self.label_date.pack(pady=10)

        # 增加点名模式选择器
        self.roll_call_mode = tk.StringVar()
        self.roll_call_mode.set("random")

        self.rb_random = tk.Radiobutton(self.tab_rollcall, text="随机点名", variable=self.roll_call_mode,
                                        value="random",
                                        command=self.set_roll_call_mode_random)
        self.rb_random.pack(pady=10)

        self.rb_sequential = tk.Radiobutton(self.tab_rollcall, text="按顺序点名", variable=self.roll_call_mode,
                                            value="sequential",
                                            command=self.set_roll_call_mode_sequential)
        self.rb_sequential.pack(pady=10)

        # 创建游标对象
        cursor = conn.cursor()
        # 从数据库中检索学生姓名
        query = "SELECT name FROM students"
        cursor.execute(query)
        # 关闭游标和连接
        cursor.close()

        self.btn_roll_call = tk.Button(self.tab_rollcall, text="点名", command=self.roll_call)
        self.btn_roll_call.pack(pady=10)

        # 增加点名结果标签
        self.label_result = tk.Label(self.tab_rollcall, font=("Helvetica", 35), text="")
        self.label_result.pack(pady=10)

        # 增加点名记录按钮
        self.roll_call_history = []

        self.btn_history = tk.Button(self.tab_rollcall, text="查看历史", command=self.view_history)
        self.btn_history.pack(pady=10)

        # 创建点名界面的控件
        self.frame_rollcall = tk.Frame(self.tab_rollcall)
        self.frame_rollcall.pack(padx=10, pady=5)

        self.lb_2 = tk.Listbox(self.frame_rollcall, width=40, height=13)
        self.lb_2.pack()

        # 主循环
        root.mainloop()
        conn.close()

    # 定义函数
    def show_students(self):
        # 创建游标对象
        cursor = conn.cursor()
        self.lb.delete(0, tk.END)
        # 执行SQL查询
        query = 'SELECT * FROM students'
        cursor.execute(query)
        # 处理查询结果
        for row in cursor:
            self.lb.insert(tk.END, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
        # 关闭游标和连接
        cursor.close()

    # 搜索全部用户
    def show_user(self):
        # 创建游标对象
        cursor = conn.cursor()
        self.lb_user.delete(0, tk.END)
        # 执行SQL查询
        query = 'SELECT * FROM user'
        cursor.execute(query)
        # 处理查询结果
        for row in cursor:
            self.lb_user.insert(tk.END, f"{row[0]} {row[1]}")
        # 关闭游标和连接
        cursor.close()

    def add_student(self):
        # 创建游标对象
        cursor = conn.cursor()
        id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        gender = self.entry_gender.get().strip()
        phone = self.entry_phone.get().strip()
        if not id or not name or not age or not gender or not phone:
            messagebox.showwarning("警告", "请输入完整的学生信息")
            return
        # 执行SQL查询
        select_query = f"SELECT * FROM students WHERE id='{id}'"
        cursor.execute(select_query)
        # 判断学号是否已经存在
        if cursor.fetchone():
            messagebox.showwarning("警告", "该学号已存在")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.entry_age.delete(0, tk.END)
            self.entry_gender.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            return
        # 执行SQL查询
        select_query_1 = f"SELECT * FROM students WHERE name='{name}'"
        cursor.execute(select_query_1)
        # 判断名字是否存在
        if cursor.fetchone():
            messagebox.showwarning("警告", "该名字已存在，如有同名请按照 _1 _2 区别")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.entry_age.delete(0, tk.END)
            self.entry_gender.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            return

        # 执行SQL插入
        insert_query = f"INSERT INTO students (id, name, age, gender, phone) VALUES ('{id}', '{name}', {age}, '{gender}', '{phone}')"
        cursor.execute(insert_query)
        conn.commit()
        self.show_students()
        messagebox.showinfo("添加成功", f"添加成功，成功添加 {name} 同学。")  # 弹出消息框提示用户
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

        # 关闭游标和连接
        cursor.close()

    def add_user(self):
        # 创建游标对象
        cursor = conn.cursor()
        username = self.entry_username.get().strip()
        passwd = self.entry_password.get().strip()
        password_hash = md5(passwd)
        if not username or not passwd:
            messagebox.showwarning("警告", "请输入完整的用户信息")
            return
        # 执行SQL查询
        select_query = f"SELECT * FROM user WHERE username='{username}'"
        cursor.execute(select_query)
        # 判断学号是否已经存在
        if cursor.fetchone():
            messagebox.showwarning("警告", "该用户已存在")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            return
        # 执行SQL查询
        select_query_1 = f"SELECT * FROM user WHERE username='{username}'"
        cursor.execute(select_query_1)
        # 判断名字是否存在
        if cursor.fetchone():
            messagebox.showwarning("警告", "该用户名已存在，如有同名请按照 _1 _2 区别")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            return

        # 执行SQL插入
        insert_query = f"INSERT INTO user (username, password_hash) VALUES ('{username}','{password_hash}')"
        cursor.execute(insert_query)
        conn.commit()
        self.show_user()
        messagebox.showinfo("添加成功", f"添加成功，成功添加 {username} 用户。")  # 弹出消息框提示用户
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        # 关闭游标和连接
        cursor.close()

    def delete_student(self):
        # 创建游标对象
        cursor = conn.cursor()
        index = self.lb.curselection()
        if not index:
            messagebox.showwarning("警告", "请选择要删除的学生")
            return
        selected_student = self.lb.get(index)
        id = selected_student.split()[0]
        # 执行SQL删除
        delete_query = f"DELETE FROM students WHERE id='{id}'"
        cursor.execute(delete_query)
        conn.commit()
        self.show_students()
        messagebox.showinfo("删除成功", "删除该条学生信息成功。")  # 弹出消息框提示用户
        # 关闭游标和连接
        cursor.close()

    # 删除用户
    def delete_user(self):
        # 创建游标对象
        cursor = conn.cursor()
        index = self.lb_user.curselection()
        if not index:
            messagebox.showwarning("警告", "请选择要删除的用户")
            return
        selected_student = self.lb_user.get(index)
        id = selected_student.split()[0]
        if id == '9999':
            messagebox.showwarning("警告", "删除失败，管理员账号无法删除！")  # 弹出消息框提示用户
        else:
            # 执行SQL删除
            delete_query = f"DELETE FROM user WHERE id='{id}'"
            cursor.execute(delete_query)
            conn.commit()
            self.show_user()
            messagebox.showinfo("删除成功", "删除该条用户信息成功。")  # 弹出消息框提示用户
            # 关闭游标和连接
            cursor.close()

    def update_student(self):
        # 创建游标对象
        cursor = conn.cursor()
        index = self.lb.curselection()
        if not index:
            messagebox.showwarning("警告", "请选择要修改的学生")
            return
        selected_student = self.lb.get(index)
        id = selected_student.split()[0]
        new_id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        gender = self.entry_gender.get().strip()
        phone = self.entry_phone.get().strip()
        # 执行SQL更新
        update_query = f"UPDATE students SET id='{new_id}', name='{name}', age={age}, gender='{gender}', phone='{phone}' WHERE id='{id}'"
        cursor.execute(update_query)

        conn.commit()
        self.show_students()
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        messagebox.showinfo("更新成功", "更新成功，学生信息已更新。")  # 弹出消息框提示用户
        # 关闭游标和连接
        cursor.close()

    # 更新用户信息
    def update_user(self):
        # 创建游标对象
        cursor = conn.cursor()
        index = self.lb_user.curselection()
        if not index:
            messagebox.showwarning("警告", "请选择要修改的用户")
            return
        selected_student = self.lb_user.get(index)
        id = selected_student.split()[0]
        username = self.entry_username.get().strip()
        if username == 'admin':
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            messagebox.showwarning("警告", "更新失败，管理员账号无法修改！")  # 弹出消息框提示用户
        else:
            passwd = self.entry_password.get().strip()
            password_hash = md5(passwd)
            # 执行SQL更新
            update_query = f"UPDATE user SET username='{username}', password_hash='{password_hash}'WHERE id='{id}'"
            cursor.execute(update_query)
            conn.commit()
            self.show_user()
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            messagebox.showinfo("更新成功", "更新成功，用户信息已更新。")  # 弹出消息框提示用户
            # 关闭游标和连接
            cursor.close()

    def search_student(self):
        # 创建游标对象
        cursor = conn.cursor()
        keyword = self.entry_search.get().strip()
        if not keyword:
            self.show_students()
            return
        self.entry_search.delete(0, tk.END)
        self.lb.delete(0, tk.END)
        # 执行SQL查询
        query = f"SELECT * FROM students WHERE id LIKE '%{keyword}%' OR name LIKE '%{keyword}%' OR gender LIKE '%{keyword}%' OR phone LIKE '%{keyword}%'"
        cursor.execute(query)
        # 处理查询结果
        for row in cursor:
            self.lb.insert(tk.END, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
        # 关闭游标和连接
        cursor.close()

    def search_user(self):
        # 创建游标对象
        cursor = conn.cursor()
        keyword = self.entry_search_user.get().strip()
        if not keyword:
            self.show_user()
            return
        self.entry_search_user.delete(0, tk.END)
        self.lb_user.delete(0, tk.END)
        # 执行SQL查询
        query = f"SELECT * FROM user WHERE username LIKE '%{keyword}%'"
        cursor.execute(query)
        # 处理查询结果
        for row in cursor:
            self.lb_user.insert(tk.END, f"{row[0]} {row[1]}")
        # 关闭游标和连接
        cursor.close()

    def set_roll_call_mode_random(self):
        self.roll_call_mode.set("random")

    def set_roll_call_mode_sequential(self):
        self.roll_call_mode.set("sequential")

    def roll_call(self):
        cursor = conn.cursor()
        # 从数据库中检索学生姓名
        query = "SELECT name FROM students"
        cursor.execute(query)
        students = [row[0] for row in cursor]

        # 为顺序点名模式定义当前索引
        if not hasattr(self, 'current_index'):
            self.current_index = 0

        if self.roll_call_mode.get() == "random":
            # 从数据库中随机选择一个学生
            query = "SELECT name FROM students ORDER BY RAND() LIMIT 1"
            cursor.execute(query)
            selected_student = cursor.fetchone()[0]
            self.current_index = 0
        else:
            # 如果 roll_call_mode 不是 "random"，则使用顺序点名模式
            # 选择列表中的下一个学生
            selected_student = students[self.current_index]
            self.current_index = (self.current_index + 1) % len(students)

        # 添加点名记录并更新界面
        self.roll_call_history.append(selected_student)
        self.label_result.config(text=selected_student)

        # 将点名记录存入数据库
        insert_query = "INSERT INTO history (date, name) VALUES (%s, %s)"
        values = (self.today, selected_student)
        cursor.execute(insert_query, values)
        conn.commit()
        # 关闭游标和连接
        cursor.close()

    def view_history(self):
        cursor = conn.cursor()
        # 从数据库中检索历史记录
        query = "SELECT date, name FROM history ORDER BY date ASC"
        cursor.execute(query)
        history_rows = cursor.fetchall()

        # 用字典按日期分组，字典的键是日期，值是该日期下的点名记录
        history_dict = {}
        for row in history_rows:
            date_str = row[0].strftime("%Y-%m-%d")
            if date_str in history_dict:
                history_dict[date_str].add(row[1])
            else:
                history_dict[date_str] = {row[1]}

        # 清空列表框并添加历史记录
        self.lb_2.delete(0, tk.END)
        query = "SELECT name FROM students"
        cursor.execute(query)
        name = []
        names = ""
        for name_set in cursor.fetchall():
            name.append(name_set[0])
        for date_str, name_set in history_dict.items():
            for i in name_set:
                # 如果该学生删除，不出现在点名历史
                if i not in name:
                    pass
                elif i in names:
                    pass
                else:
                    names = names + i + '、'
            self.lb_2.insert(tk.END, f"{date_str}：{names[:-1]}")
        # 关闭游标和连接
        cursor.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x300')  # 设置窗口大小
    root.title('登陆/注册')  # 设置窗口标题
    app = LoginRegisterFrame(master=root)
    app.mainloop()
