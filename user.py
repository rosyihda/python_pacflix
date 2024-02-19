from tabulate import tabulate


class User:
    # data user pacflix
    data = {
        1:["Ihda", 'Basic Plan', 12, "ihda123"],
        2:["Rosy", 'Standard Plan', 24, "rosy123"],
        3:["Agus", 'Premium Plan', 4, "agus123"]
    }

    # # data plan pacflix
    header = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
    table_plan = [
        [True,True,True,'can_stream'],
        [True,True,True,'can_download'],
        [True,True,True,'has_SD'],
        [False,True,True,'has_HD'],
        [False,False,True,'has_UHD'],
        [1,2,4, 'num_of_devices'],
        ['3rd party movie only', 'Basic Plan Content + Sports (F1, Football, Basketball)',
         	'Basic Plan + Standard Plan + PacFlix Original Series or Movie', 'content'],
        [120_000, 160_000, 200_000, 'price']
    ]

    def __init__(self):
        """
            init class user
        """
        self.username = None
        self.duration = None
        self.current_plan = None
        self.kode_referal = None
    
    def login(self, username):
        """
            Fungsi untuk melakukan logiin bedasarkan usename
            lalu set nilai plan, duration, kode referal berdasarkan username

            input: username
            output: -
        """
        self.username = username
        for key, data_user in self.data.items():
            if data_user[0] == username:
                self.duration = data_user[2]
                self.current_plan = data_user[1]
                self.kode_referal = data_user[3]
                break
            else:
                self.duration = None
                self.current_plan = None
                self.kode_referal = None
                   

    def check_plan(self):
        """
            fungsi untuk menampilkan data plan pacflicks

            input : None
            Output : Print data plan
        """
        print("Data Plan Pacflix")
        print(tabulate(self.table_plan,self.header))

    def check_plan_user(self):
        """
        funsgi untuk menampilkan plan user yang login

        input: none
        output: print informasi plan
        """
        print(f"plan dari user {self.username}")
        try:
            if(self.current_plan in self.header):
                if(self.current_plan == "Basic Plan"):
                   service = [ [row[0], row[-1]] for row in self.table_plan]
                   header = ['Basic Plan','Services']

                elif(self.current_plan == "Standard Plan"):
                    service = [ [row[1],row[-1]] for row in self.table_plan]
                    header = ['Standard Plan','Services']
                elif(self.current_plan == "Premium Plan"):
                    service = [ [row[2],row[-1]] for row in self.table_plan]
                    header = ['Premium Plan','Services']
                print(tabulate(service,header))
        except Exception as e:
            print(e)
    
    def upgrade(self,new_plan):
        """
            Fungsi untuk melakukan upgrade plan user

            input: new_plan
            output: harga dari new_plan
        """
        try:
            idx_current_plan = self.header.index(self.current_plan)
            idx_new_plan = self.header.index(new_plan)
            if(idx_current_plan < idx_new_plan):
                if(self.duration > 12):
                    total = self.table_plan[7][idx_new_plan] - (self.table_plan[7][idx_new_plan]*0.05)
                else:
                    total = self.table_plan[7][idx_new_plan]
                print(f"selamat anda upgrade ke {new_plan}, bayar {total}")
                self.current_plan = new_plan
            elif(idx_current_plan == idx_new_plan):
                print("anda sudah berlangganan plan tersebut")
            else:
                print("anda tidak bisa melakukan downgrade")
        except Exception as e:
            print(e)

    def subcribe(self,plan,kode_referal):
        """
            Fungsi untuk mendaftarkan plan user baru

            input: plan, kode referal
            output: total bayar user
        """
        if(plan in self.header):
            self.current_plan = plan
            self.duration = 1
            self.kode_referal = self.username+'123'

            list_referal =  [row[-1] for row in self.data.values()]
            idx_plan = self.header.index(plan)
            if(kode_referal in list_referal):
                total = self.table_plan[7][idx_plan] -(self.table_plan[7][idx_plan]*0.04)
            else:
                total = self.table_plan[7][idx_plan]
            # last_idx
            # input(last_idx+1 dan data)
            print(f"selamat anda telah berlangganan {plan}, bayar {total}")
        else:
            print("tidak ada plan tersebut")

    