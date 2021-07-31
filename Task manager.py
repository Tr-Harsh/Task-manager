from tkinter import *
import os
import subprocess

class app:
	def __init__(self,master):
		i=0
		master.minsize(width=500, height=800)
		master.maxsize(width=500, height=800)
		# os.system("rm qwer*")
		# os.system("/usr/bin/timeout --foreground --signal=SIGINT 5 airodump-ng mon0 -w qwer")
		
		cc=0
		def read_file():
			cc=0
			f = open('qwer-01.csv',"r")
			line = f.readlines()
			a=[[]]*len(line)
			for i in range(len(line)):
				if line[i].split(',')[0]=="Station MAC":
					cc=i-1
					#print(cc)
					break
				a[i] = line[i].split(',')
			f.close()
			return a,cc

		def reset():
			for i in range(2,cc):
				c[i].destroy()
			pw.destroy()
			pb.destroy()
			pc.destroy()
			dd.destroy()
			s.destroy()
			time_l.destroy()
			e1.destroy()
			bssid = ""
			channel = ""
			#print("aa")
			ap=app(root)
		
		def print_name():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][13].lstrip())
					break
		def print_bssid():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][0].lstrip())
					break
		def print_channel():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][3].lstrip())
					break

		def ddos():
			os.system("timeout --signal=SIGINT 5 airodump-ng wlan0mon -w aaaaaa.csv")
			for i in range(cc):
				if var[i].get()==1:
					bssid=a[i][0]
					channel=a[i][3]
					break
			# os.system("airmon-ng start wlan0mon "+channel)
			print("aireplay-ng --deauth 1000 -h '1c:39:47:25:33:cc' -a '"+bssid+"'")
			# os.system("aireplay-ng --deauth "+ e1.get() +" -h 'E0:94:67:69:C6:E3' -a '"+bssid+"' wlan0mon")
			reset()






		
		def createlist_appcommands():
		    dtfile_dir = "/usr/share/applications"
		    dtfile_list = [item for item in os.listdir(dtfile_dir) if item.endswith(".desktop")]
		    commands = []
		    for item in dtfile_list:
		        try:
		            with open(dtfile_dir+"/"+item) as data:
		                searchlines = data.readlines()
		                command = [line for line in searchlines if line.startswith("Exec=")
		                           and not "NoDisplay=true\n" in searchlines
		                            ][0].replace("Exec=", "").replace("\n", "").split("/")[-1].split(" ")[0]
		            commands.append(command)
		        except Exception:
		            pass
		    return commands + [trace_symlinks(item) for item in commands if not trace_symlinks(item)== None]
		
		def trace_symlinks(command):
		    target = subprocess.Popen(["which", command], stdout=subprocess.PIPE)
		    location = (target.communicate()[0].decode("utf-8")).split("\n")[0]                                                          
		    check_filetype = subprocess.Popen(["file", location], stdout=subprocess.PIPE)
		    filetype = (check_filetype.communicate()[0].decode("utf-8")).split("\n")[0]
		    if "symbolic link" in filetype:
		        return filetype.split("/")[-1].replace("' ", "")
		    else:
		        pass
		
		def createlist_runningprocs():
		    processesb = subprocess.Popen(["ps", "-e"], stdout=subprocess.PIPE)
		    process_listb = (processesb.communicate()[0].decode("utf-8")).split("\n")
		    linked_commands = [(item, item[24:]) for item in process_listb][1:]
		    applist = createlist_appcommands()
		    print("Processes, related to applications:\n  PID TTY"+" "*10+"TIME CMD")
		    matches = []
		    abc = []
		    for item in applist:
		        for i in range(0, len(linked_commands)):
		            if item[:15] in linked_commands[i][1] and len(item[:15])/len(linked_commands[i][1]) > 0.5:
		                matches.append(i)
		    matches = sorted(matches)
		    for i in range(0, len(linked_commands)):
		        if i in matches:
			    #abc[i] = abc[i].split(',')
		            abc.append(linked_commands[i][0].split(' '))

		    return abc,len(abc)









		#a,cc=createlist_runningprocs()
		
		a,cc=createlist_runningprocs()
		print(a)
		l=Label(root, text = "List of Processes running now : ", font = ('times',15)).grid(row=0, sticky = W)
		var = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar]
		#print(cc)
		c=[None]*cc
		for i in range(0,cc):
			c[i]=Checkbutton(root, text=a[i][-1], variable = var[i], font = ('times',13))
			c[i].grid(row=i+1, sticky=W)
		i=i+1		
		pw=Button(root, text = "Get PID", font = ('times', 20), command = print_name)
		pw.grid(row=i+2, sticky=W)
		pb=Button(root, text = "Refresh", font = ('times', 20), command = reset)
		pb.grid(row=i+3, sticky=W)


		e1 = Entry(master)

		e1.grid(row=i+8, column = 0, sticky='we')
		print(a)
		print(cc)

root = Tk()
ap = app(root)
root.mainloop()
