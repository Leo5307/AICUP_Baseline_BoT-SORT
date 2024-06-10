import os
import shutil

def copy_txt_files(source_dir, dest_dir):
    # 確保目標文件夾存在，如果不存在就創建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # 遍歷源目錄及其子目錄
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.txt'):
                # 構建完整的文件路徑
                file_path = os.path.join(root, file)
                # 複製文件
                shutil.copy(file_path, dest_dir)
                print(f'Copied {file_path} to {dest_dir}')

# 使用示例
source_directory = './runs/detect_test/real_final_comparing'  # 源目錄路徑
destination_directory = '../public/real_final_comparing'  # 目標目錄路徑
copy_txt_files(source_directory, destination_directory)
