# Big casework problem

# Spam fill in 2-in-a-rows
# If each row/col only has one thing, you can just duplicate it

# Fill arbitrarily:
# X X X 
# X X X
# X X X 

# Row/col is full with nothing else: Just copy
# 1 X X 
# 1 X X
# 1 X X 

# ROW/COL IS FULL LEAVING A 4x4 SHAPE (which always happens since 2 in a rows are filled): Increment the cols by 1 (the diff that it needs) and move them up
# 1 X X 
# 2 X X
# 3 5 7 

# Increment the cols by 3 and move them down
# 14 15 16
# XX 12 XX
# XX 9  XX

# If there are 7 Xs: it will either be a full row or you can just copy up the columns and fill in the remaining row
# 1 X X
# X 3 X
# X X X

# In this case, if their difference is odd, it might be impossible? not sure tho. maybe generate a random number until it works for this case
# 1 X X
# X X X
# X X 4

# If there are 6 Xs and its not a full row/col (im p sure this is the only possibility that doesn't fulfill any of the things above): Random generate a number until it works.
# 1 X X
# X 5 X
# X X 8

# 14 X X
# X X 16
# X 18 X