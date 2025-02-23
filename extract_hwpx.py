import os
import shutil
import tempfile
import fire


def extract_section0_xml(zip_path: str = r"1p.hwpx",
                         destination_path: str = r"./extraction/Contents/"):
    """
    압축 파일에서 Contents/section0.xml 파일만 추출하여 지정된 경로로 복사합니다.

    :param zip_path: 압축 파일의 경로
    :param destination_path: 복사할 대상 경로
    """
    # 임시 디렉토리 생성
    with tempfile.TemporaryDirectory() as temp_dir:
        # 압축 해제
        shutil.unpack_archive(zip_path, temp_dir, format="zip")

        # 추출할 파일 경로 지정
        target_files = [os.path.join(temp_dir, "Contents", "section0.xml"),
                        os.path.join(temp_dir, "Contents", "header.xml")]

        # 파일이 존재하는지 확인
        for file in target_files:
            if os.path.isfile(file):
                shutil.copy(file, destination_path)
                print(f"{file} 파일을 추출하였습니다.\n{destination_path}")
            else:
                raise FileNotFoundError(f"{file} 파일이 존재하지 않습니다.")


if __name__ == "__main__":
    fire.Fire(extract_section0_xml)
