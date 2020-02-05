



# Your code here
.5



# Your code here
p_w = .6
p_o = .1
.3*p_w

# Your code here
p_g95 = .35
p_g98 = .25
p_diesel = .4
p_f_g95 = .6
p_f_g98 = .5
p_f_d = .3
#buys 95 AND fills tank
p_g95 * p_f_g95 #.21
#next customer fills tank p(buys_gas) * p(fills it)
p_f_n_g95 = p_g95 * p_f_g95
p_f_n_g98 = p_g98 * p_f_g98
p_f_n_d = p_diesel * p_f_d
p_f_n_g95 + p_f_n_g98 + p_f_n_d





# Your code here
p_ao = .4
p_bo = .25
p_co = .35
#all flights
p_ao * p_bo * p_co
#at least one
p_atleast_1 = p_ao + p_bo + p_co
#exactly one
#p_ao - p_ao_n_bo - p_ao_n_co + p_bo - p_ao_n_bo - p_bo_n_co + p_co - p_ao_n_co - p_bo_n_co - 3 * (p_ao_n_bo_n_co)
