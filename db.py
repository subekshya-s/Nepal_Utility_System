import psycopg2
from psycopg2 import sql

""" When we call the db the  a object is created and sotring it in a variable . python creates the new mwmory [ Database Object ]  after that __init__ is run whill will fill the object
with data [ Database Object ]
   db_name = "coderush"
   user = "postgres"
   conn = (will be created)
   cursor = (will be created) """


class Database:
    def __init__(self):
        print("\n Initializing Database Setup...")

        self.db_name = "coderush"
        self.user = "postgres"
        self.password = "12345"
        self.host = "localhost"
        self.port = "5432"

        #Check/Create Database
        self.create_database_if_not_exists()

        #connect to the database
        self.connect()

        #create table
        self.create_table()

    #create DB if nolt exists
    def create_database_if_not_exists(self):
        print("\n Checking database........")

        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            conn.autocommit = True
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (self.db_name,)

            )
            exists = cursor.fetchone()

            if exists:
                print(f" Database '{self.db_name}' already exists")

            else:
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(
                        sql.Identifier(self.db_name)
                    )
                )
                print(f"Database '{self.db_name}' created")

            cursor.close()
            conn.close()

        except Exception as e :
            print("Error:",e)

    # Step 2: Connect
    def connect(self):
        print("\n Step 2: Connecting...")

        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

            """Internally this happens:

            DNS/host resolution:
            localhost → IP 127.0.0.1
            Socket creation:
            Python opens a TCP connection to PostgreSQL on port 5432.
            Authentication:
            PostgreSQL receives username/password.
            If correct → connection allowed.
            Session setup:
            PostgreSQL allocates a server-side session object for this connection.
            Sends back a “ready” message to Python.
            conn object in Python:
            Stores:
            socket info (where to send queries)
            session state (transaction status, autocommit)
            internal buffers
            Lets Python send queries to PostgreSQL easily.

            🔹 Think of self.conn as a live channel between your Python program and PostgreSQL."""

            self.cursor = self.conn.cursor()
            """Internally:

Python creates a cursor object in memory.
The cursor object keeps track of:
Query execution state (current row, result set)
Bindings for parameters (%s placeholders)
Reference to the connection (self.conn) it belongs to
Every time you call cursor.execute("SQL query"):
psycopg2 sends the SQL to the database via the connection
PostgreSQL executes the query
Results are stored in a server-side buffer
cursor.fetchall() fetches them into Python memory

🔹 Think of the cursor as a pointer / controller that says:
“I want to send queries through this connection and fetch results row by row.”"""
            print(" Connected successfully")

        except Exception as e:
            print(" Connection failed:", e)

    #step 3 : Create Table
    def create_table(self):
        print("\n Step 3 : Creating table.....")

        query = """
        CREATE TABLE IF NOT EXISTS students(
            roll_no SERIAL PRIMARY KEY,
            name VARCHAR(100),
                dob DATE,
                education VARCHAR(100),
                address TEXT
        );
        """

        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Tabel ready")

        except Exception as e :
            print("Error:",e)
        
    #INSERT
    def insert_student(self,name,dob,education,address):
        query = """
        INSERT INTO students(name,dob,education,address)
        VALUES (%s,%s,%s,%s)"""

        try:
            self.cursor.execute(query,(name,dob,education,address))
            self.conn.commit()
            print("student inserted")

        except Exception as e :
            print("insert error:",e)


    #SELECT 
    def view_students(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            data =self.cursor.fetchall()

            print(f"{len(data)} record(s) found")
            return data
        
        except Exception as e:
            print(" Fetch error:", e)
            return []

    def update_student(self, roll_no, name=None, dob=None, education=None, address=None):
        print("\n Updating student...")

        try:
            query = """
            UPDATE students
            SET name = COALESCE(%s, name),
                dob = COALESCE(%s, dob),
                education = COALESCE(%s, education),
                address = COALESCE(%s, address)
            WHERE roll_no = %s
            """

            self.cursor.execute(query, (name, dob, education, address, roll_no))
            self.conn.commit()

            print(" Student updated")

        except Exception as e:
            print(" Update error:", e)

    #delete
    def delete_student(self, roll_no):
        print("\n Deleting student...")

        try:
            query = "DELETE FROM students WHERE roll_no = %s"
            self.cursor.execute(query, (roll_no,))
            self.conn.commit()

            print(" Student deleted")

        except Exception as e:
            print(" Delete error:", e)

    # CLOSE
    def close(self):
        self.cursor.close()
        self.conn.close()
        print(" Connection closed")


db = Database()  #db  ───────▶  [ Database Object in memory ]