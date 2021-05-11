import matplotlib.pyplot as plt

class charts:
       
    def bar_chart(x,y,nama,judul):
        #figure mirip dg window
        gambar=plt.figure()
        #plot itu garis x dan y
        axes=gambar.add_subplot(1,1,1)
        plt.suptitle(judul)
        warna = ['#8EE1E4', '#E48EA4', '#8EE490','#E4E38E', '#A48EE4']

        #x range nilai di sb x, dari 0 sampai sekian
        #y range nilai di sumbu y
        #tick_label untuk ganti nama di sb x
        axes.bar(x,y,tick_label=nama, color=warna) 
    
    def line_chart(nilai,nama,judul):
        gambar=plt.figure()
        diagram=gambar.add_subplot(1,1,1)
        plt.suptitle(judul)
        warna = ['#8EE1E4', '#E48EA4', '#8EE490','#E4E38E', '#A48EE4']
        #nama label di sb x
        #nilai tiap titik di sb y
        #C3 untuk range warna
        diagram.plot(nama,nilai,'C3')
    
    def pie_chart(label, ukuran, judul):
        gambar=plt.figure()
        plt.suptitle(judul)
        explode=(0,0.1,0,0)
        warna = ['#8EE1E4', '#E48EA4', '#8EE490','#E4E38E', '#A48EE4']

        diagram=gambar.add_subplot(1,1,1)
        #explode untuk kayak pizza yg kepisah
        #autopct untuk nentuin persentasi, brapa banyak angka di blakang koma
        diagram.pie(ukuran, explode=explode,labels=label,colors=warna, autopct='%1.1f%%',startangle=90)

        #memastikan gambarnya lingkaran
        diagram.axis('equal')

#contoh
d1=charts.bar_chart([1,2,3,4], [3,6,7,25], ["A","B","C","D"], "diagram batang")
d2=charts.line_chart([3,4,7,25],[3,7,7,25],"diagram garis")
d3=charts.pie_chart(["A","B","C","D"], [3,6,7,25], "diagram anu")

#untuk nampilin semua diagram
plt.show()