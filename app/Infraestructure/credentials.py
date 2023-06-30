import environ

INI_DB = environ.secrets.INISecrets.from_path_in_env("DB_CRED")


@environ.config(prefix="APP")
class CredentialsConfig:

    @environ.config(prefix="DB")
    class DBConfig:
        """
        DBConfig Class representing the configuration to access the database
        """
        host: str = INI_DB.secret(name="host", default=environ.var())
        port: int = INI_DB.secret(name="port", default=environ.var())
        name: str = INI_DB.secret(name="dbname", default=environ.var())
        user: str = INI_DB.secret(name="user", default=environ.var())
        password: str = INI_DB.secret(name="password", default=environ.var())

    db = environ.group(DBConfig)


def get_conf():
    return environ.to_config(AppConfig)
