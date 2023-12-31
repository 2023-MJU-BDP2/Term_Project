import os
import csv
import json

# JSON 데이터를 CSV 파일에 변환하는 함수
def convert_json_to_csv(json_data, csv_file_path):
    # CSV 파일 열기
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        file_name = json_data["images"][0]["file_name"]
        image_id = json_data["images"][0]["image_id"]
        metainfo = json_data["categories"][0]["metainfo"]
        name = json_data["categories"][0]["name"]
        location1 = metainfo["location1"]
        location2 = metainfo["location2"]
        Type1 = metainfo["Type1"]
        Type2 = metainfo["Type2"]
        name_kr = metainfo["name_kr"]
        location = metainfo["add"]
        writer.writerow([file_name, image_id, name, location1, location2, Type1, Type2, name_kr, location])


if __name__ == "__main__":
    # CSV 파일 경로
    csv_file_path = 'landmarks_img_labels.csv'
    folder_path = "./라벨링데이터/서울특별시"
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        headers = ['filename', 'imgId', 'name', 'location1', 'location2', 'type1', 'type2', 'nameKr', 'location']
        writer.writerow(headers)
    folder_list = os.listdir(folder_path)
    for landmark in folder_list:
        for root, dirs, files in os.walk(f"{folder_path}/{landmark}"):
            for file_name in files:
                if file_name.endswith('.json'):
                    json_file_path = os.path.join(root, file_name)
                    # JSON 파일 읽기
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        json_data = json.load(json_file)
                        # JSON 데이터를 CSV 파일로 변환
                        convert_json_to_csv(json_data, csv_file_path)
    print("JSON 데이터가 성공적으로 CSV 파일로 변환되었습니다.")
