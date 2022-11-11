#기호와 함께 출력하기
print("#기호와 함께 출력하기")
output_a="{:f}".format(52.273)
output_b="{:15f}".format(52.273)
output_c="{:+15f}".format(52.273)
output_d="{:+015f}".format(52.273)


print(output_a)
print(output_b)
print(output_c)
print(output_d)

#소수점 아래 자릿수 지정하기
print("#소수점 아래 자릿수 지정하기")
output_j="{:15.3f}".format(52.273)
output_z="{:15.2f}".format(52.273)
output_g="{:15.1f}".format(52.273)

print(output_j)
print(output_z)
print(output_g)


#의미없는 소수점 제거하기
print("#의미없는 소수점 제거하기")
output_q=52.0
output_w="{:g}".format(output_q)
print(output_q)
print(output_w)