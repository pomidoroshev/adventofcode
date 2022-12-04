def run(inp):
    m_1 = 0
    m_2 = 0
    m_3 = 0

    cur = 0
    for line in inp:
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

    return m_1 + m_2 + m_3
