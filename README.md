## 專案介紹
1. 此專案為2024 AICUP——AI驅動出行未來：跨相機多目標車輛追蹤競賽（模型組）的參考專案
2. 大部分實作過程參考自主辦方的Baseline（https://github.com/ricky-696/AICUP_Baseline_BoT-SORT）
3. 如有不詳盡之處，敬請參照主辦方的github

## 硬體環境的兩種選擇：
1. Google Colab:（這篇Readme.md所使用的方式，可直接執行 AICUP_main.ipynb）
CPU: Intel(R) Xeon(R) CPU @ 2.20GHz
GPU: NVIDIA L4   
預估訓練fast reid 模型所需時間：8小時
預估訓練 yolov7 模型所需時間： 36小時
預估推論訓練集所需時間：4小時
預估推論測試集所需時間：4小時

2.桌機（需要按照 Baseline 的方式自行調整各檔案的路徑）
CPU: AMD Ryzen 9 7950X 16-Core Processor
GPU: NVIDIA GeForce RTX 4090
預估訓練fast reid 模型所需時間：8小時
預估訓練 yolov7 模型所需時間： 12小時
預估推論訓練集所需時間：2小時
推論測試集所需時間：2小時

## 如何使用該專案：
方法：
### 依照比賽規定以下以 google colab 的方式來介紹。
1. 下載程式碼中的AICUP_main.ipynb 並到google colab 執行。
### 詳細介紹各模塊輸入輸出 & AICUP_main.ipynb 的具體實作：
1. 安裝Anaconda與環境設定
    - 按照Baseline的環境需求將環境裝好
    - 這裡只需按照順序執行即可
2. 下載以及處理比賽資料集
    - 這裡需要確保google drive中有訓練集、測試集、預訓練模型和為了復現結果所需要的我訓練好的模型
    - 大致上資料結構如下所示：
    ![image](https://github.com/Leo5307/AICUP_Baseline_BoT-SORT/assets/116941598/964c6851-0377-44c4-ad8c-4f4d09a461ea)

    - 訓練集（dataset.zip）可從[官網](https://tbrain.trendmicro.com.tw/Competitions/Details/33)下載（下載後重命名為datasets.zip）
    - 測試集（32_33_AI_CUP_testdataset.zip）可從[官網](https://tbrain.trendmicro.com.tw/Competitions/Details/33)下載
    - 預訓練模型可參照baseline程式的方式在這裡下載[mot20_sbs_S50.pth](https://drive.google.com/file/d/1KqPQyj6MFyftliBHEIER7m_OrGpcrJwi/view?usp=sharing)
    - 我訓練好的模型可在這裡下載：[leaderboard_model.zip](https://drive.google.com/file/d/1WO7YUq7r0f2Y3P_pfchfKEZz1ITajptc/view?usp=sharing)
    - 自此專案的準備工作就此結束,這階段按照順序執行即可
        - ``` fast_reid/datasets/generate_AICUP_patches.py ``` 負責將訓練集轉換成訓練 fast_reid 模型所需的資料
        - ``` yolov7/tools/AICUP_to_YOLOv7.py ``` 負責將訓練集轉換成訓練 YOLO 模型所需的資料
3. 訓練 fast_reid 模型：
    - 按照順序執行即可訓練 fast_reid 模型，其結果儲存在：/content/AICUP_Baseline_BoT-SORT/logs/AICUP/sbs_S50_2_report_v2 裡面會包含權重檔(model_final.pth)以及模型的設定檔案（config.yaml），會在之後推論時用到。

4. 訓練 YOLO 模型：
    - 按照順序執行即可訓練 YOLO 模型，其結果儲存在：/content/AICUP_Baseline_BoT-SORT/runs/train/yolov7-AICUP 裡面會包含權重檔(best.pt)以及一些評估指標，會在之後推論時用到。

5. 推論訓練集階段：
    - 利用寫好的``` track_all_timestamps_report.sh ```對模型進行推論
    - --weight 參數指的是 YOLO 的權重檔案 (best.pt)
    - --source-dir 需要的是訓練集的路徑
    - --fast-reid-config 需要的是fast-reid 的模型設定檔（config.yaml）
    - --fast-reid-weights 需要的是fast-reid 的模型權重檔(model_final.pth)
    - 以上皆預設使用我訓練好的模型，如要使用上面訓練好的模型，需要自行更換路徑

6. 推論測試集階段：
    - 同推論訓練集階段，但這裡的source-dir 指定的是測試集


