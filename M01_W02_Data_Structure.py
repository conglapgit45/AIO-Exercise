"""1. Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1"""
def find_max(lst):
    result = -999999
    for x in lst:
        if x > result:
            result = x
    return result


def sliding(num_list, k):
    result = []
    begin = 0
    end = k
    while len(num_list[begin: end]) == k:
        result.append(find_max(num_list[begin: end]))
        begin += 1
        end += 1
    print(result)


"""2. Thực hiện theo các yêu cầu sau.
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện"""
def count_letter(text):
    list_letter = []
    dict_letter = dict()
    for c in text:
        if c not in list_letter:
            list_letter.append(c)
    for k in list_letter:
        cnt = 0
        for c in text:
            if c == k:
                cnt += 1
        dict_letter[k] = cnt
    print(dict_letter)


"""3. Thực hiện theo các yêu cầu sau.
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện."""
def count_word(dir):
    list_word = []
    dict_word = dict()
    with open(dir, "r") as f:
        data = f.read().lower().split()
        for word in data:
            if word not in list_word:
                list_word.append(word)
        for k in list_word:
            cnt = 0
            for word in data:
                if word == k:
                    cnt += 1
            dict_word[k] = cnt
    print(dict_word)


"""4. Khoảng cách Levenshtein.
Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein."""
def distance_levenshtein(source, target):
    """Bước 1: Xây dựng ma trận lưu trữ có số hàng là M và số cột là N. Trong đó M là số lượng
  các ký tự trong từ source + 1, N là số lượng các ký tự trong từ target + 1. Vì vậy với ví dụ
  'yu' và 'you', ta có ma trận được biểu diễn như hình 1. Ký hiệu '#' đại diện cho chuỗi rỗng.
  Gọi là ma trận D."""
    d = []
    m = len(source) + 1
    n = len(target) + 1
    for i in range(m):
        d.append([])
        for j in range(n):
            d[i].append([])

    """Bước 2: Hoàn thiện hàng và cột đầu tiên. Với hàng đầu tiên, các giá trị đại diện cho chuỗi
bắt đầu là chuỗi '#' và phép biến đổi là thêm (insert) từ chuỗi '#' thành '#', '#y', '#yo',
'#you' lần lượt là 0, 1, 2, 3 tương ứng với ô D[0, 0], D[0, 1], D[0, 2], D[0, 3]. Với cột đầu tiên,
các giá trị đại diện cho chuỗi '#', '#y', '#yu' và phép biến đổi là xoá (delete) để thu được
chuỗi '#' lần lượt là: 0, 1, 2 tương ứng với ô D[0, 0], D[1, 0], D[2, 0]. Ta được hình 2."""
    for i in range(m):
        d[i][0] = i
    for j in range(n):
        d[0][j] = j

    """Bước 3. Tính toán các giá trị với các ô còn lại trong ma trận."""
    for i in range(1, m):
        for j in range(1, n):
            if min(d[i][0], d[0][j]) == 0:
                d[i][j] = max(d[i][0], d[0][j])
            else:
                sub_cost = 0
                if source[i - 1] == target[j - 1]:
                    sub_cost = d[i - 1][j - 1]
                else:
                    sub_cost = d[i - 1][j - 1] + 1
                d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, sub_cost)

    """Bước 4: Sau khi hoàn thành ma trận, chúng ta đi tìm đường đi từ ô cuối cùng D[2, 3] có giá
trị là 1. Vì vậy khoảng cách chỉnh sửa từ source: 'yu' sang thành target: 'you' là 1. Đầu tiên
ký tự 'y' giữ nguyên sau đó thực hiện 1 phép thêm ký tự 'o' vào sau ký tự 'y' và cuối cùng
ký tự 'u' được giữ nguyên."""
    for i in range(m):
        print(d[i])
    print(f"Edit distance: {d[m - 1][n - 1]}")


if __name__ == "__main__":
    # 01.
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    sliding(num_list, k)

    # 02.
    text = "Happiness"
    count_letter(text)

    # 03.
    dir = "P1_data.txt"
    count_word(dir)

    # 04.
    source = "hola"
    target = "hello"
    ee = 0
    distance_levenshtein(source, target)
