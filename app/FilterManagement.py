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
            "_"                          : 0,  # なし
            "_dotArt"                    : 1,  # ドット絵風
            "_mosaic"                    : 2,  # モザイク
            "_subColor"                  : 3,  # 減色
            "_threshold"                 : 4,  # 二値化
            "_edge"                      : 5,  # エッジ検出
            "_gauss"                     : 6,  # ガウスぼかし
            "_medianFilter"              : 7,  # メディアンフィルター
            "_WBComic"                   : 8,  # 漫画風(白黒)
            "_pencil"                    : 9,  # 鉛筆風
            "_AIAnimeArt"                : 10, # AIアニメ風
            "_creatingColoringBook"      : 11, # 塗り絵化
            "_stylization"               : 12, # 水彩画風
            "_grayScale"                 : 13, # グレースケール
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
        elif (filterNum == self.filterDict["_edge"]): # エッジ検出の説明のとき
            return self.exFilterEdge()
        elif (filterNum == self.filterDict["_gauss"]): # ガウスぼかしの説明のとき
            return self.exFilterGauss()
        elif (filterNum == self.filterDict["_medianFilter"]): # メディアンフィルターの説明のとき
            return self.exFilterMedianFilter()
        elif (filterNum == self.filterDict["_WBComic"]): # 漫画風(白黒)の説明のとき
            return self.exFilterMedianFilter()
        elif (filterNum == self.filterDict["_pencil"]): # 鉛筆風の説明のとき
            return self.exFilterPencil()
        elif (filterNum == self.filterDict["_AIAnimeArt"]): # AIアニメ風の説明のとき
            return self.exFilterAIAnimeArt()
        elif (filterNum == self.filterDict["_creatingColoringBook"]): # 塗り絵化の説明のとき
            return self.exFilterCreatingColoringBook()
        elif (filterNum == self.filterDict["_stylization"]): # 水彩画風の説明のとき
            return self.exFilterStylization()
        elif (filterNum == self.filterDict["_grayScale"]): # グレースケールの説明のとき
            return self.exFilterGrayScale()
        else:
            assert(False)

    # 1モザイクの説明
    def exFilterMosaic(self):
        return "モザイクの説明"

    # 2二値化の説明
    def exFilterThreshold(self):
        return "二値化の説明"

    # 3減色の説明
    def exFilterSubColor(self):
        return "減色の説明"

    # 4ドット絵風の説明
    def exFilterDotArt(self):
        return "ドット絵風の説明"
    
    # 5エッジ検出の説明
    def exFilterEdge(self):
        return "エッジ検出の説明"
    
    # 6ガウスぼかしの説明
    def exFilterGauss(self):
        return "ガウスぼかしの説明"
    
    # 7メディアンフィルターの説明
    def exFilterMedianFilter(self):
        return "メディアンフィルターの説明"

    # 8漫画風(白黒)の説明
    def exFilterWBComic(self):
        return "漫画風(白黒)の説明"

    # 9鉛筆風の説明
    def exFilterPencil(self):
        return "鉛筆風の説明"

    # 10AIアニメ風の説明
    def exFilterAIAnimeArt(self):
        return "アニメ風の説明"

    # 11塗り絵化の説明
    def exFilterCreatingColoringBook(self):
        return "塗り絵化の説明"

    # 12水彩画風の説明
    def exFilterStylization(self):
        return "水彩画風の説明"

    # 13グレースケールの説明
    def exFilterGrayScale(self):
        return "グレースケールの説明"

    # 説明を取得する
    def getExplain(self):
        return self.__explain

