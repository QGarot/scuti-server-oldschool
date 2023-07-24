import mysql.connector


class Database:
    def __init__(self, host: str, user: str, password: str, name: str):
        """
        Classe permettant de gérer les actions effectuées sur une base de données.
        :param host:
        :param user:
        :param password:
        :param name:
        """
        self.host = host
        self.user = user
        self.password = password
        self.name = name

        self.connection = None
        self.cursor = None

    def prepare_db(self):
        """
        Méthode permettant de se connecter à la base de données et de positionner l'objet curseur.
        A appeler avant chaque action !
        :return:
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            port=3306,
            user=self.user,
            database=self.name,
            password=self.password
        )

        self.cursor = self.connection.cursor()

    def close_connection(self):
        """
        Méthode permettant de fermer la connexion à la base de données et le curseur.
        A appeler après chaque action !
        :return:
        """
        self.cursor.close()
        self.connection.close()
        self.cursor = None
        self.connection = None

    def get(self, sql: str) -> []:
        self.prepare_db()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.close_connection()
        return result

    def set(self, sql: str):
        pass

    def update(self, table_name: str, attributes: dict, sql_condition: str):
        """
        Permet de mettre à jour les données d'une table.
        -> {"fied": new value of this field}
        :param table_name:
        :param attributes: de type dict. Un couple (a, b) de ce dictionnaire
        signifie que les valeurs correspondant à l'attribut "a" prendront la
        nouvelle valeur "b"
        :param sql_condition:
        :return:
        """
        attr_str = ""
        first = True
        for couple in attributes.items():
            if first:
                attr_str = attr_str + couple[0] + " = '" + str(couple[1]) + "'"
                first = False
            else:
                attr_str = attr_str + ", " + couple[0] + " = '" + str(couple[1]) + "'"

        self.prepare_db()
        sql = "UPDATE " + table_name + " SET " + attr_str + " WHERE " + sql_condition
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()

    def insert(self, table_name, structure, values):
        """
        Permet d'insérer de nouveaux enregistrements dans une table.
        :param table_name:
        :param structure:
        :param values:
        :return: None
        """

        self.prepare_db()

        sql = "INSERT INTO " + table_name + " " + structure + " VALUES " + str(values)
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()
