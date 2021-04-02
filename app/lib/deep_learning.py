import fasttext as ft
from janome.tokenizer import Tokenizer

MODEL_NAME = "model.bin"

TAG = [
    ["__label__1", "政治・経済[AI]"],
    ["__label__2", "テクノロジー[AI]"],
    ["__label__3", "ゲーム[AI]"],
    ["__label__4", "グルメ[AI]"]
    ]

def learning(input_file_path):
    """
    学習データからモデルを生成

    Parameters
    ----------
    input_file_path : String
        学習データ

    None
        なし
    """

    model = ft.train_supervised(input_file_path, epoch=1000, loss="hs")
    model.save_model(MODEL_NAME)

class predict:
    """
    学習モデルによる予測を行う
    """

    def __init__(self):
        # 学習モデル読み込み
        self.classifier = ft.load_model(MODEL_NAME)
        
        # 分かち書き
        self.tokenizer = Tokenizer()

    def tag_judgment(self, sentence):
        """
        文章からタグを判定する

        Parameters
        ----------
        sentence : String
            判定対象の文章

        Returns
        -------
        tag : String
            判定したタグ
        """

        words = self.__get_surfaces(sentence)

        estimate = self.classifier.predict(text=[words], k=1)

        for tag in TAG:
            if tag[0] in estimate[0][0][0]:
                return tag[1], estimate
        else:
            return "Other"

    def __get_surfaces(self, sentence):
        """
        文章を分かち書きに変換する

        Parameters
        ----------
        sentence : String
            判定対象の文章

        Returns
        -------
        String
            判定対象の文章を分かち書きした文字列
        """

        separate = list(map(lambda s: s.surface, self.tokenizer.tokenize(sentence)))

        return " ".join(separate)

if __name__ == '__main__':
    pre = predict()
    tag = pre.tag_judgment("ASUS 『TUF Gaming VG27AQL1A』 レビューチェック ～強化版となる27インチ/IPS/WQHD/170Hzゲーミングモニター ")

    print(tag)