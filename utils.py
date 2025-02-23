import os
import lxml
import shutil
from PIL import Image
import tempfile
import fire


def md2hwpx(markdown: str | os.PathLike, output: str, style: str):
    """마크다운 파일이나 텍스트를 입력받아 한글 문서로 만드는 함수

    Args:
        markdown (str | os.PathLike): 변환하고 싶은 마크다운 문서의 경로나 텍스트
        output (str): 내보낼 파일 경로
        style (str): 참고할 스타일
    """

    # 1. 마크다운 파싱

    # 2. 기본적인 한글 문서 리소스 만들기

    # 2. 1. 루트 요소 만들기
    with tempfile.TemporaryDirectory() as temp_dir:
        folders = ["Contents", "META-INF", "Preview"]

        for folder in folders:
            os.makedirs(os.path.join(temp_dir, folder), exist_ok=True)

        # 2. 1. 1. settings.xml
        _get_setting()

        # 2. 1. 2. version.xml
        _get_version()

        # 2. 1. 3. mimetype
        _get_mimetype(temp_dir)

        # 2. 2. Preview 요소 만들기

        # 2. 2. 1. Preview 이미지 만들기
        _create_prvimage(temp_dir)

        # 2. 2. 2. Preview 텍스트 만들기
        _create_prvtext(markdown, temp_dir)

        # 2. 3. META-INF 요소 만들기

        # 2. 3. 1. container.rdf
        # 2. 3. 2. container.rdf
        # 2. 3. 3. container.rdf
    return


def _create_prvimage(path):
    # Preview 폴더 경로 생성
    preview_dir = os.path.join(path, "Preview")
    os.makedirs(preview_dir, exist_ok=True)  # 폴더가 없으면 생성

    # 이미지 파일 경로
    file = os.path.join(preview_dir, "PrvImage.png")

    # 765 x 1024 크기의 빈 하얀색 이미지 생성
    img = Image.new('RGB', (765, 1024), color='white')

    # 이미지 저장
    img.save(file)
    return None


def _create_prvtext(md_text, path):
    file = os.path.join(path, "Preview", "PrvText.text")
    with open(file, "r", encoding='UTF-8') as f:
        f.write(md_text)
    return None


def extract_style(hwpx_path: str, type: str = "yaml"):
    """
    한글 문서를 인자로 받아서 스타일을 경로에 추가하는 함수

    Args:
        hwpx_path (str): 한글 문서의 파일 경로, hwpx나 sty 파일을 인자로 받는다.
    """

    # 1. 입력 받은 한글 문서가 실제로 경로상에 존재하는지 확인하고, 없다면 에러 발생
    if not os.path.exists(hwpx_path):
        print(f"{hwpx_path} not exists !")
        raise ValueError

    # 2.
    # 10. 기본 스타일 지정 폴더가 있다면 거기에 저장하고 없다면 만들어서 저장
    return


def extract_section0_xml(zip_path, destination_path):
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
