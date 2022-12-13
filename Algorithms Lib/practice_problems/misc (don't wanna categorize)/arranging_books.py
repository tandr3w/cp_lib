sequence = list(input())
l_count = 0
m_count = 0
s_count = 0
for i in sequence:
    if i == "L":
        l_count += 1
    if i == "M":
        m_count += 1
    if i == "S":
        s_count += 1

# Define how many of each type should be in each section
l_section = sequence[:l_count]
m_section = sequence[l_count:l_count+m_count]
s_section = sequence[l_count+m_count:]

# Have to swap once for each letter thats not an L but is in the L section. Then, have to swap once for each letter in the M section that isn't an M. But if there's an L in the M section, step 1 does this already, so subtract the number of times that can happen.
print(l_count-l_section.count('L') + m_count-m_section.count("M")-min(m_section.count("L"), l_section.count("M")))