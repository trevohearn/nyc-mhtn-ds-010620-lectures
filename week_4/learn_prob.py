# Your code here

p_c = .5
p_d = 1/6
p_c * p_d

# Your code here
p_c = 8/10
p_c * p_c * p_c

# Your code here
p_c = .7
p_c_n_s = .35
p_s_g_c = None #p(a) + p(b) - p(anb) = 1
#.7 + p(s) =1.35 - .7 = .65 = p(s)
p_s = .65
#p(a | b) = p(a n b) / p(b)
p_c_n_s / p_s

# Your code here
4/52 * 3/52

p_bad = 5/100
1 - (p_bad + p_bad + p_bad)

# Your code here
a = list(range(1,7))
sample_space = [(x, y) for x in a for y in a]
truths = [(x[0] + x[1] == 8 and (x[0] > 4 or x[1] > 4)) for x in sample_space]
truths.count(True) / len(sample_space)

# Your code here
p_b_given_a = None
p_b_not_given_a = None
p_a_given_b = None
p_a_not_given_b = None
