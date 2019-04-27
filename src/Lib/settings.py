import yaml
"""
設定(data.yml)読み込み用クラス
"""
class settings:
    @staticmethod
    def get():
        """設定を返却
        Args:
        Returns:
            dict?のはず
        """
        with open('data.yml') as file:
            token = yaml.safe_load(file)
        return token