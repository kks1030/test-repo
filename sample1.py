print('김경식', '201900543','컴퓨터전자시스템공학부')
if3 if3
def same(a):
    a=list(a.lower())
    if a==reversed(a):
        return True
    else:
        print(a)
        return False
def main():
    a=input()
    if same(a)==True:
        print('yes')
    else:
        print('no')
main()
