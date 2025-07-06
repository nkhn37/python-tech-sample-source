"""python-oracledbモジュール
oracledb モジュールを用いたOracleデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-oracledb-oracle-connection/
"""

import configparser

import oracledb


class DbConnectOracle:
    """Oracle DBアクセスクラス"""

    def __init__(self, mode: str = "thin", client_lib_dir: str = None) -> None:
        """コンストラクタ

        Args:
            mode: "thin" または "thick"
            client_lib_dir: Thick モードの場合は、Oracle Client のライブラリパス
        """
        # モード判定
        if mode == "thick":
            if client_lib_dir is None:
                raise ValueError(
                    "Thick モードでは client_lib_dir の指定が必要です。"
                )
            oracledb.init_oracle_client(client_lib_dir)
        elif mode != "thin":
            raise ValueError(
                "mode は、'thin' または 'Thick' を指定してください。"
            )

        # iniファイルの読み込み
        config_db = configparser.ConfigParser()
        config_db.read("dbconfig.ini")

        # 設定の読み込み
        host = config_db["ORACLE_DB_SERVER"]["host"]
        port = int(config_db["ORACLE_DB_SERVER"]["port"])
        service_name = config_db["ORACLE_DB_SERVER"]["service"]
        user = config_db["ORACLE_DB_SERVER"]["user"]
        password = config_db["ORACLE_DB_SERVER"]["password"]

        # DSN の作成
        self.dsn = oracledb.makedsn(host, port, service_name=service_name)

        # 接続の確立
        self.con = oracledb.connect(
            user=user,
            password=password,
            dsn=self.dsn,
        )
        self.cursor = self.con.cursor()

    def execute_non_query(self, sql: str, bind_var: dict = None) -> None:
        """SQL 実行メソッド
        (CREATE / INSERT / UPDATE / DELETE 用)

        Args:
            sql: 実行SQL
            bind_var: バインド変数

        Returns: None

        """
        # SQLの実行
        if bind_var is None:
            self.cursor.execute(sql)
        else:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)

    def execute_query(
        self, sql: str, bind_var: dict = None, count: int = 0
    ) -> list:
        """SQL 実行メソッド
        (SELECT 用)

        Args:
            sql: 実行SQL
            bind_var: バインド変数
            count: データ取得件数

        Returns: 取得結果リスト

        """
        # SQLの実行
        if bind_var is None:
            self.cursor.execute(sql)
        else:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)

        columns = [col[0] for col in self.cursor.description]
        self.cursor.rowfactory = lambda *args: dict(zip(columns, args))

        # 取得結果を返却 (件数指定がある場合は、指定された件数分返却)
        return (
            self.cursor.fetchall()
            if count == 0
            else self.cursor.fetchmany(count)
        )

    def commit(self) -> None:
        """コミット

        Returns: None

        """
        self.con.commit()

    def rollback(self) -> None:
        """ロールバック

        Returns: None

        """
        self.con.rollback()

    def __del__(self) -> None:
        """デストラクタ

        Returns: None

        """
        self.cursor.close()
        self.con.close()


if __name__ == "__main__":
    pass
