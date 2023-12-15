import dearpygui.dearpygui as dpg
import sqlite3
import csv


def getHeader(name_csv):
    """Return the header of the csv file given
    Arguments:
    name_csv -- path to the csv file.
    """
    with open(name_csv, "r") as file:
        csv_reader = csv.reader(file)
        return next(csv_reader)


def createTable(table, cursor, headers):
    """Create table on database
    Arguments:
    table -- name of the table to be created
    cursor -- instance of the cursor
    headers -- columnds of the database
    """
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS {table} (
    {", ".join([f"{header} TEXT" for header in headers])})"""
    cursor.execute(create_table_sql)


def inserDataTable(file, table, cursor):
    """Insert data to table on database
    Arguments:
    file -- path to the csv file
    table -- name of de the table
    """
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            query = f"""INSERT INTO {table} VALUES (
            {", ".join(["?" for _ in row])})"""
            cursor.execute(query, row)


dpg.create_context()

dpg.create_viewport(title='Cancer Connector', width=900, height=600)

with dpg.font_registry():
    default_font = dpg.add_font("JetBrainsMonoNerdFont-Regular.ttf", 20)
    second_font = dpg.add_font("JetBrainsMonoNerdFont-Regular.ttf", 20)

def callback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print(app_data['file_path_name'])

def createTableFuente(sender, app_data):
    conn = sqlite3.connect("cancer.db")
    cursor = conn.cursor()
    headers = getHeader(app_data['file_path_name'])
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS fuente (
    {", ".join([f"{header} TEXT" for header in headers])})"""
    cursor.execute(create_table_sql)
    conn.commit()
    with open(app_data['file_path_name'], "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            query = f"""INSERT INTO fuente VALUES (
            {", ".join(["?" for _ in row])})"""
            cursor.execute(query, row)
    conn.commit()
    conn.close()

def createTablePaciente(sender, app_data):
    conn = sqlite3.connect("cancer.db")
    cursor = conn.cursor()
    headers = getHeader(app_data['file_path_name'])
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS paciente (
    {", ".join([f"{header} TEXT" for header in headers])})"""
    cursor.execute(create_table_sql)
    conn.commit()
    with open(app_data['file_path_name'], "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            query = f"""INSERT INTO paciente VALUES (
            {", ".join(["?" for _ in row])})"""
            cursor.execute(query, row)
    conn.commit()
    conn.close()

def createTableTumores(sender, app_data):
    conn = sqlite3.connect("cancer.db")
    cursor = conn.cursor()
    headers = getHeader(app_data['file_path_name'])
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS tumores (
    {", ".join([f"{header} TEXT" for header in headers])})"""
    cursor.execute(create_table_sql)
    conn.commit()
    with open(app_data['file_path_name'], "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            query = f"""INSERT INTO tumores VALUES (
            {", ".join(["?" for _ in row])})"""
            cursor.execute(query, row)
    conn.commit()
    conn.close()

with dpg.file_dialog(directory_selector=False, show=False, callback=createTableFuente, id="import_fuentes", width=700 ,height=400):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))

with dpg.file_dialog(directory_selector=False, show=False, callback=createTablePaciente, id="import_pacientes", width=700 ,height=400):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))

with dpg.file_dialog(directory_selector=False, show=False, callback=createTableTumores, id="import_tumores", width=700 ,height=400):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))

with dpg.window(label="Fuentes", width=300, height=200):
    dpg.bind_font(default_font)
    dpg.add_button(label="Importar Fuentes", callback=lambda: dpg.show_item("import_fuentes"))

with dpg.window(label="Pacientes", width=300, height=200, pos=(301, 0)):
    dpg.add_button(label="Importar Pacientes", callback=lambda: dpg.show_item("import_pacientes"))

with dpg.window(label="Tumores", width=300, height=200, pos=(601, 0)):
    dpg.add_button(label="Importar Tumores", callback=lambda: dpg.show_item("import_tumores"))

with dpg.window(label="Inserta datos a las tablas", width=900, height=400, pos=(0, 201), no_resize=True, no_move=True, no_close=True, no_collapse=True):
    dpg.add_button(label="Insertar datos a Fuentes")
    dpg.add_button(label="Insertar datos a Pacientes")
    dpg.add_button(label="Insertar datos a Tumores")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
