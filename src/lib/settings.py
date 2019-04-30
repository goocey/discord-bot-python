import yaml
"""
設定(data.yml)読み込み用クラス
"""
class settings:
    @staticmethod
    def get_setting():
        """設定を返却
        Args:
        Returns:
            dict?のはず
        """
        with open('data.yml', encoding="utf-8") as file:
            token = yaml.safe_load(file)
        return token['SETTINGS']

    @staticmethod
    def get_role_list():
        """設定を返却
        Args:
        Returns:
            dict?のはず
        """
        with open('data.yml', encoding="utf-8") as file:
            token = yaml.safe_load(file)
        return token['ROLE_LIST']

    @staticmethod
    def get_role_help():
        """設定を返却
        Args:
        Returns:
            dict?のはず
        """
        with open('data.yml', encoding="utf-8") as file:
            token = yaml.safe_load(file)
        return token['ROLE_HELP']