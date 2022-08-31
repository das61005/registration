### 使用probreg實作liver registration
<img src="https://github.com/das61005/registration/blob/main/image/same_rotate.png" width="400" height="400" /><img src="https://github.com/das61005/registration/blob/main/image/dif_rotate.png" width="400" height="400"/><br/>

   ```
   cd examples
   ```
   
## 預處理
### mask_to_pointcloud.py

將需要做registration的dicom nii.gz抽樣點座標(預設為50取1)並寫入txt

input:

兩個dicom的nii.gz檔

output:

before_mask.txt(第一個dicom的抽樣點座標)

after_mask.txt(第二個dicom的抽樣點座標)

補充:第10,11行換成自己檔案的路徑
```
   python mask_to_pointcloud.py
```
## registration
### registratoin.py

將兩個點雲迭代至最近點並輸出轉移矩陣、位移量、縮放量

input:

before_mask.txt

after_mask.txt

output:

transform_matrix_rot.txt(轉移矩陣)

transform_matrix_t.txt(位移量)

scale.txt(縮放量)
```
   registratoin.py
```
## 檢視效能
### mask_transform.py

展示registration狀況
```
   python mask_transform.py
```
