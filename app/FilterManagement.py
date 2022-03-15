#　2022/03/03 北谷海斗
# フィルターを管理するクラスです。（今後翻訳機能とかもつけたいかも)
# 0->japanese
# 1->English...てきな
# フィルターと番号の辞書を作って、番号から説明を取り出す。
class FilterManagement:
    #コンストラクタ
    def  __init__(self, filterName):
        # フィルターを追加したら以下の辞書に追加する
        self.filterDict = {
            "_" : 0,
            "_dotArt" : 1,
            "_mosaic" : 2,
            "_subColor" : 3,
            "_threshold" : 4,
            "_gauss" : 5,
        }
        self.__explain = self.explainFilter(self.filterDict[filterName])            

    #　各フィルターの説明
    def explainFilter(self, filterNum):
        if (filterNum == self.filterDict["_dotArt"]): # ドット絵風の説明のとき
            return self.exFilterDotArt()
        elif (filterNum == self.filterDict["_mosaic"]): # モザイクの説明のとき
            return self.exFilterMosaic()
        elif (filterNum == self.filterDict["_subColor"]): # 減色の説明のとき
            return self.exFilterSubColor()
        elif (filterNum == self.filterDict["_threshold"]): # 二値化の説明のとき
            return self.exFilterThreshold()
        elif (filterNum == self.filterDict["_gauss"]): # ガウスぼかしの説明のとき
            return self.exFilterGauss()

    # モザイクの説明
    def exFilterMosaic(self):
        return "モザイクの説明"

    # 二値化の説明
    def exFilterThreshold(self):
        return "二値化の説明"

    # 減色の説明
    def exFilterSubColor(self):
        return "減色の説明"

    # ドット絵風の説明
    def exFilterDotArt(self):
        return "ドット絵風の説明"

    # ガウスぼかしの説明
    def exFilterGauss(self):
        return "ガウスぼかしの説明"

    # 説明を取得する
    def getExplain(self):
        return self.__explain

    # レスポンスで返す各フィルターに対するパラメータを元の辞書に追加する
#    def addRetBaseDict(self, filterNum, retDict, addDict):
