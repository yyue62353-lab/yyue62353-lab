import argparse

from plagiarism import cosine_similarity


def read_file(file_path):
    """读取文本文件。"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{file_path}")
    except OSError as error:
        raise OSError(f"无法读取文件：{error}")


def write_result(file_path, similarity):
    """将查重结果写入文件。"""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"论文相似度：{similarity * 100:.2f}%\n")
    except OSError as error:
        raise OSError(f"无法写入结果文件：{error}")


def main():
    parser = argparse.ArgumentParser(
        description="论文查重程序"
    )
    parser.add_argument("original", help="原文文件路径")
    parser.add_argument("plagiarism", help="待检测论文文件路径")
    parser.add_argument("output", help="结果输出文件路径")

    args = parser.parse_args()

    try:
        original_text = read_file(args.original)
        plagiarism_text = read_file(args.plagiarism)

        similarity = cosine_similarity(
            original_text,
            plagiarism_text
        )

        write_result(args.output, similarity)

        print(f"论文相似度：{similarity * 100:.2f}%")

    except (FileNotFoundError, OSError) as error:
        print(f"错误：{error}")


if __name__ == "__main__":
    main()
