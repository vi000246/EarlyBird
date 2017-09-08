# encoding: utf-8
import numpy as np
import numpy
import cv2
import sys
import collections
from matplotlib import gridspec
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import random, os

reload(sys)
sys.setdefaultencoding("utf-8")
class Image:
    '''
        如果type=url
        getimg參數要傳入requests回傳的content
        如果type=local
        getimg參數要傳入圖片本地路徑
        '''

    def __init__(self, getimg, type='url'):
        #  設置 matplotlib 中文字體
        self.font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
        #  儲存檔名
        self.imageName = 'fileName'
        # #  儲存路徑
        # self.Path = Path
        #  用來儲放分割後的圖片邊緣坐標(x,y,w,h)
        self.arr = []
        #  將每個階段做的圖存起來 用來debug
        self.dicImg = collections.OrderedDict()
        #  將圖片做灰階
        # self.im = cv2.imread(Path + "\\" + ImgName)
        if type == 'url':
            image = np.asarray(bytearray(getimg), dtype="uint8")
            self.im = cv2.imdecode(image, cv2.IMREAD_COLOR)
        elif type == 'local':
            self.im = cv2.imread(getimg)
            self.dicImg.update({"原始圖片": self.im.copy()})

        #  閾值化
    def threshold(self):
        # 115 是 threshold，越高濾掉越多
        # 255 是當你將 method 設為 THRESH_BINARY_INV 後，高於 threshold 要設定的顏色
        # 反轉黑白 以利輪廓識別
        gray_image = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        retval, self.im = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
        self.dicImg.update({"閾值化": self.im.copy()})

    #  將圖片顯示出來
    def showImg(self, img=None):
        if img is None:
            img = self.im

        cv2.imshow(self.imageName, img)
        cv2.namedWindow(self.imageName, cv2.WINDOW_NORMAL)
        #  調整視窗 讓標題列顯示出來
        cv2.resizeWindow(self.imageName, 250, 60)
        cv2.waitKey()
    #  將多個圖片顯示在一個figure
    def showImgEveryStep(self,):
        diclength = len(self.dicImg)
        if diclength > 0:
            fig = plt.figure(figsize=(10, 10))
            gs = gridspec.GridSpec(diclength+1, 6)

            # 依序列出dict物件裡的圖片
            for index, key in enumerate(self.dicImg):
                #  如果不是list物件 就是圖片 可以呼叫imshow
                if not isinstance(self.dicImg[key], list):
                    ax = fig.add_subplot(gs[index, :6])
                    ax.imshow(self.dicImg[key], interpolation='nearest')
                    ax.set_title(key, fontproperties=self.font)
                else:
                    try:
                        for i, img in enumerate(self.dicImg[key]):
                            ax = fig.add_subplot(gs[index, i])
                            ax.imshow(img, interpolation='nearest')
                    except IndexError:
                        pass

            plt.tight_layout()
            plt.show()
        else:
            print '圖片數字陣列為空'

if __name__ == '__main__':
    path = "D:\\CaptchaExample"
    # 隨機選一張圖片
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    x = Image(path+'\\'+random_filename,'local')
    x.threshold()
    x.showImgEveryStep()

