def run():
    m_1 = 0
    m_2 = 0
    m_3 = 0

    cur = 0
    with open('input.txt') as f:
        for line in map(str.strip, f):
            if not line:
                if cur >= m_1:
                    m_1, m_2, m_3 = cur, m_1, m_2
                elif m_1 >= cur >= m_2:
                    m_2, m_3 = cur, m_2
                elif cur >= m_3:
                    m_3 = cur
                cur = 0
                continue
            cur += int(line)

    print(m_1 + m_2 + m_3)

if __name__ == '__main__':
    run()
