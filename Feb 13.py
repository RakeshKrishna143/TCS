class Account:
    def __init__(self,name,balance):
        self.name = name 
        self.balance= balance
    def deposit_money(self,amount):
        self.balance +=amount
        return self.balance
    def withdraw_money(self,amount):
        self.balance-=amount
        return self.balance

class UpdateAccount:
    def __init__(self,cname,acc_list):
        self.cname = cname

    def depOrWithdrawal(self,name,dep_or_withdraw,amount):
        for i in acc_list:
            if i.name  == name:
                if dep_or_withdraw == 'deposit':
                    return i.deposit_money(amount)
                else:
                    if i.balance - amount >=1000:
                        return i.withdraw_money(amount)
                    else:
                        return 'Insufficient balance'
                    
if __name__ =='__main__':
    t = int(input())
    acc_list = []
    for i in range(t):
        name = input()
        balance = int(input())
        acc_list.append(Account(name,balance))
    name = input()
    dep_or_withdraw = input()
    amount = int(input())
    u = UpdateAccount('abc bank',acc_list)
    res = u.depOrWithdrawal(name,dep_or_withdraw,amount)
    print(res)
