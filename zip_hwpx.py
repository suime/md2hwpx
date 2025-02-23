import shutil
import os
import fire


def compress_to_zip(source_path: str = r".\extraction",
                    destination_dir: str = r".\TEST", name: str = "TEST"):
    """
    주어진 경로의 파일과 폴더를 000.zip으로 압축합니다.

    :param source_path: 압축할 파일 또는 폴더 경로
    :param destination_dir: 압축 파일이 저장될 경로
    :return: 생성된 압축 파일 경로
    """
    # 압축 파일 경로 설정 (확장자 제외한 이름만 전달)
    temp_zip_path = os.path.join(destination_dir, name)

    try:
        shutil.make_archive(temp_zip_path, 'zip', root_dir=source_path)

        # 확장자를 .hwpx로 변경
        hwpx_file_path = temp_zip_path + ".hwpx"

        # 파일이 이미 존재하는 경우 숫자를 붙여 새로운 이름 생성
        counter = 1
        while os.path.exists(hwpx_file_path):
            hwpx_file_path = f"{temp_zip_path}_{counter}.hwpx"
            counter += 1

        os.rename(temp_zip_path + ".zip", hwpx_file_path)
        print(f"압축 완료: {hwpx_file_path}")
        return hwpx_file_path
    except Exception as e:
        print(f"한글파일 출력 실패: {e}")
        return None


if __name__ == "__main__":
    fire.Fire(compress_to_zip)
