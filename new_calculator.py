def str_calculate(a, b, operacja):
  if operacja == 'concat':
    return a + b
  if operacja == 'awb':
    return a in b
  if operacja == 'last_sign_in_b_shbe_a':
    return a[0] in b[-1]
   #print(b[-1])
  if operacja == 'last_sign_in_a_shbe_b':
    return a[-1] in b[0]
  return 0