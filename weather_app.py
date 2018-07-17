# importing modules
from tkinter import *
from PIL import Image,ImageTk
root= Tk()
import requests
import datetime
api = "https://api.openweathermap.org/data/2.5/forecast?appid=c58cdabba6bb5ffe073a4b9023b8a57d&units=metric&q="
root.title('''Weather app''')
root.geometry('500x500')
def init_stage():
    menuM = Menu(root)
    root.config(menu=menuM)
    labL_1 =Label(root,text='Enter your city :',font='times 12 bold',fg='blue')
    labL_1.grid(row=1,column = 0)
    city=Entry(root)
    city.grid(row=1,column=1)
    def show_detail():
        city_n=city.get()
        url = api+city_n    
        weath = requests.get(url).json()
        cityL= Label(root,text= city_n,font='times 16  underline',fg='blue',bg='yellow')
        cityL.grid(row=3,column=1)
        x=0
        show_weather(weath,x) 
        show_temprature(weath,x)
        show_humidity(weath,x)
        show_wind(weath,x)
    submit_1 = Button(root,text='Show Weather',command=show_detail)
    submit_1.grid(row =2,column=1,ipadx=5,ipady=5)
# function to show weather for next day
    def next_day():
        r = Toplevel()
        r.geometry('400x300')
        s = datetime.datetime.today()
        modified_date = s + datetime.timedelta(days=1)
        date_tom=datetime.datetime.strftime(modified_date, "%d/%m/%Y")
        date_L=Label(r,text=date_tom,font = 'times 16 bold underline')
        date_L.grid(row= 1,column=1)
        city_n=city.get()
        url = api+city_n    
        weath = requests.get(url).json()
        x=4
        def show_weath(weath,x):
            pic_=weath['list'][x]['weather'][0]['icon']
            pic_n=str(pic_)+'.png'
            fl=Image.open(pic_n)
            im=ImageTk.PhotoImage(fl)
            imL= Label(r,image=im)
            imL.image=im
            imL.grid(row=1,column=0)
            weath_textL=Label(r,text='Weather :',font='times 16  underline',fg='red')
            weath_textL.grid(row=2,column=0)
            weath_type = weath['list'][x]['weather'][0]['main']
            weathL= Label(r,text= weath_type,font='times 16 bold',fg='blue')
            weathL.grid(row=2,column=1)
            weath_textL=Label(r,text='Description :',font='times 16  underline',fg='red')
            weath_textL.grid(row=3,column=0)
            weath_description = weath['list'][x]['weather'][0]['description']
            weath_desc= Label(r,text= weath_description,font='times 16  bold',fg='blue')
            weath_desc.grid(row=3,column=1)
            return weathL,weath_desc    
        def show_temp(weath,x):
            temp_text=Label(r,text='Temprature :',font='times 16  underline',fg='red')
            temp_text.grid(row=4,column=0)
            temp = weath['list'][x]['main']['temp']
            s= str(temp)+str(' °C')
            tempL= Label(r,text=s,font='times 16  bold',fg='blue')
            tempL.grid(row=4,column=1)
            return tempL
        def show_humi(weath,x):
            humid_text=Label(r,text='Humidity :',font='times 16  underline',fg='red')
            humid_text.grid(row=5,column=0)
            humid = weath['list'][x]['main']['humidity']
            s= str(humid)+str(' %')
            humidL= Label(r,text= s,font='times 16  bold',fg='blue')
            humidL.grid(row=5,column=1)
            return humidL
        def show_windd(weath,x):
            wind_text=Label(r,text='Wind Speed :',font='times 16  underline',fg='red')
            wind_text.grid(row=6,column=0)
            wind= weath['list'][x]['wind']['speed']
            s= str(wind)+str(' m/s')
            windL= Label(r,text= s,font='times 16  bold',fg='blue')
            windL.grid(row=6,column=1)
            return windL
        show_weath(weath,x)
        show_temp(weath,x)
        show_humi(weath,x)
        show_windd(weath,x)
        quit_1 = Button(r,text='EXIT THIS WINDOW',command=r.destroy)
        quit_1.grid(row =8,column=1,padx=10,pady=10,ipadx=5,ipady=5)
        r.mainloop()
# functions to show  today's weather        
    def show_weather(weath,x):
        try:
            date=datetime.datetime.today().strftime('%d-%m-%Y')
            date_L=Label(root,text=date,font = 'times 16 bold underline')
            date_L.grid(row= 4,column=1)
            # selecting weather image
            pic_id=weath['list'][x]['weather'][0]['icon']
            pic_name=str(pic_id)+'.png'
            j=Image.open(pic_name)
            img=ImageTk.PhotoImage(j)
            imgL= Label(root,image=img)
            imgL.image=img
            imgL.grid(row=4,column=0)
            weath_textL=Label(root,text='Weather :',font='times 16  underline',fg='red')
            weath_textL.grid(row=6,column=0)
            weath_type = weath['list'][x]['weather'][0]['main']
            weathL= Label(root,text= weath_type,font='times 16 bold',fg='blue')
            weathL.grid(row=6,column=1)
            weath_textL=Label(root,text='Description :',font='times 16  underline',fg='red')
            weath_textL.grid(row=7,column=0)
            weath_description = weath['list'][x]['weather'][0]['description']
            weath_desc= Label(root,text= weath_description,font='times 16  bold',fg='blue')
            weath_desc.grid(row=7,column=1)
            return weathL,weath_desc
        except Exception as err:
            er=str(type(err))+'the program stopped because of an error'
            err_L =Label(root,text= er)
            err_L.grid()     
    def show_temprature(weath,x):
        temp_text=Label(root,text='Temprature :',font='times 16  underline',fg='red')
        temp_text.grid(row=8,column=0)
        temp = weath['list'][x]['main']['temp']
        s= str(temp)+str(' °C')
        tempL= Label(root,text=s,font='times 16  bold',fg='blue')
        tempL.grid(row=8,column=1)
        return tempL
    def show_humidity(weath,x):
        humid_text=Label(root,text='Humidity :',font='times 16  underline',fg='red')
        humid_text.grid(row=9,column=0)
        humid = weath['list'][x]['main']['humidity']
        s= str(humid)+str(' %')
        humidL= Label(root,text= s,font='times 16  bold',fg='blue')
        humidL.grid(row=9,column=1)
        return humidL
    def show_wind(weath,x):
        wind_text=Label(root,text='Wind Speed :',font='times 16  underline',fg='red')
        wind_text.grid(row=10,column=0)
        wind= weath['list'][x]['wind']['speed']
        s= str(wind)+str(' m/s')
        windL= Label(root,text= s,font='times 16  bold',fg='blue')
        windL.grid(row=10,column=1)
        submit_2 = Button(root,text='Check Weather For Tommorow',command=next_day)
        submit_2.grid(row =13,column=1,ipadx=5,ipady=5)
        return windL
 # generating Menu   
    fileM = Menu(menuM)
    menuM.add_cascade(label='File',menu=fileM)
    fileM.add_command(label='Exit',command=root.destroy)
    root.mainloop()
init_stage()   # calling our main function for whole gui functioning

