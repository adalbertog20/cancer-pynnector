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


def inserDataTable(file, table):
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


if __name__ == "__main__":
    conn = sqlite3.connect("cancer.db")
    cursor = conn.cursor()

    # Paciente Table Fill with paciente.csv file
    createTable("paciente", cursor, getHeader("paciente/paciente.csv"))
    conn.commit()
    inserDataTable("paciente/paciente.csv", "paciente")
    conn.commit()

    # Tumor Table Fill with tumor.csv file
    createTable("tumor", cursor, getHeader("tumor/tumor.csv"))
    conn.commit()
    inserDataTable("tumor/tumor.csv", "tumor")
    conn.commit()

    # fuente Table Fill with fuente.csv file
    createTable("fuente", cursor, getHeader("fuente/fuente.csv"))
    conn.commit()
    inserDataTable("fuente/fuente.csv", "fuente")
    conn.commit()
