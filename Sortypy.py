import time
import shutil
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




def loadJsons():
    with open("Config.json") as c:
        Config = json.load(c)
    with open("Rules.json") as r:
        Rules = json.load(r)

    return Config, Rules

config, rules = loadJsons()

def log(msg):
    logfile = "SortyPyLog.txt"
    with open(logfile, "a") as f:
        f.writelines('\n')
        f.writelines(str(msg))

def files():
    files = [ ]
    files = os.listdir(config["Config"]["Source_Folder"])
    return files

def Copy(src, dest):
    if os.path.isfile(dest)!= True:
        shutil.copy(src, dest)
        log("Copyed: "+str(src)+ " to " + str(dest))
    
def Move(src, dest,rename,replace):
    if rename == True:
        destsplit = dest.split(".")
        i=1
        while os.path.isfile(destsplit[0]+"_"+str(i)+destsplit[1]) == True:
            i+=1
        newdest = destsplit[0]+"_"+str(i)+destsplit[1]
        shutil.move(src,newdest)
        log("Moved and Renamed: "+ str(src)+ " to ", str(newdest))
    else:
        if os.path.isfile(dest)==True:
            if replace == True:
                shutil.move(src,dest)
                log("File moved and Overwritten Existing File: "+ str(src)+ " to " +str(dest))
            else:
                log("File exists in Destination unable to move: " + str(src))
        else:
            shutil.move(src,dest)
            log("File moved: "+ str(src)+ " to " +str(dest))
    files()

def partial_name(file, rule):
    src = config["Config"]["Source_Folder"]+"/"+file
    dest = rule["Destination"]+"/"+file
    match = rule["Rule_Params"]
    if len(match) ==1:
       isin = match in file 
       if isin == True:
            if rule["Rule_exec"]== "Move":
               Move(src,dest,rule["Rename"],rule["Replace"])
            elif rule["Rule_exec"]== "Copy":
               Copy(src,dest)
    elif len(match) >1:
        for i in range(0,len(match)):
            isin = match[i] in file 
            if isin == True:
                if rule["Rule_exec"]== "Move":
                    Move(src,dest,rule["Rename"],rule["Replace"])
                elif rule["Rule_exec"]== "Copy":
                    Copy(src,dest)
    else:
        log("error partial name Rule_Params")
    


def exact_name(file,rule):
    src = config["Config"]["Source_Folder"]+"/"+file
    dest = rule["Destination"]+"/"+file
    match = rule["Rule_Params"]
    if len(match) ==1:
         if file == match:
            if rule["Rule_exec"]== "Move":
                Move(src,dest,rule["Rename"],rule["Replace"])
            elif rule["Rule_exec"]== "Copy":
                Copy(src,dest)
    elif len(match) >1:
        for i in range(0,len(match)):
            if file == match[i]:
                if rule["Rule_exec"]== "Move":
                    Move(src,dest,rule["Rename"],rule["Replace"])
                elif rule["Rule_exec"]== "Copy":
                    Copy(src,dest)
    else:
        log("error exact name Rule_Params")

def extention(file,rule):
    src = config["Config"]["Source_Folder"]+"/"+file
    dest = rule["Destination"]+"/"+file
    match = rule["Rule_Params"]
    if len(match) ==1:
        isin = str(match) in str(file)
        if isin == True:
            if rule["Rule_exec"]== "Move":
                    Move(src,dest,rule["Rename"],rule["Replace"])
            elif rule["Rule_exec"]== "Copy":
                    Copy(src,dest)
    elif len(match) >1:
        for i in range(0,len(match)):
            isin = str(match[i]) in str(file)
            if isin == True:
                if rule["Rule_exec"]== "Move":
                    Move(src,dest,rule["Rename"],rule["Replace"])
                elif rule["Rule_exec"]== "Copy":
                    Copy(src,dest)
    else:
        log("error extentions Rule_Params")

def RuleCheck(file,rule):
    ruleType = rule["Rule_Type"]
    if ruleType == "extention":
        extention(file,rule)
    elif ruleType == "partial":
        partial_name(file,rule)
    elif ruleType == "exact":
        exact_name(file,rule)
    else:
       log("invalid rule type: " + str(rule))

def Rules(file):
    if len(rules["Rules"]) ==0:
        log("no rules")
    elif len(rules["Rules"])!=1:
            
        for i in range(1,len(rules["Rules"])+1):
            rule = rules["Rules"]["Rule-"+str(i)]
            if rule["Active"] == True:
                ruleType = rule["Rule_Type"]
                RuleCheck(file,rule)
    elif len(rules["Priority_Rules"])==1:
            rule = rules["Rules"]["Rule-1"]
            if rule["Active"] == True:
                ruleType = rule["Rule_Type"]
                RuleCheck(file,rule)

def Priority_Rules(file):
    if len(rules["Priority_Rules"]) ==0:
        log("no  Priroity rules")
    elif len(rules["Priority_Rules"])!=1:
        for i in range(1,len(rules["Priority_Rules"])+1):
            rule = rules["Priority_Rules"]["Rule-p-"+str(i)]
            if rule["Active"] == True:
                ruleType = rule["Rule_Type"]
                RuleCheck(file,rule)
    elif len(rules["Priority_Rules"])==1:
            rule = rules["Priority_Rules"]["Rule-p-1"]
            if rule["Active"] == True:
                ruleType = rule["Rule_Type"]
                RuleCheck(file,rule)

            

def Run_Rules():

    newFiles = files()
    print (newFiles)
    priorityLen = len(rules["Priority_Rules"])
    if len(newFiles)!= 1:
        filesLen =len(newFiles)
        for i in range(0,filesLen):
            if priorityLen != 0:
                Priority_Rules(newFiles[i])
            checkfile = files()
            checkfilebool = newFiles[i] in checkfile
            if checkfilebool == True:
                Rules(newFiles[i])
    else:
        if priorityLen != 0:
             Priority_Rules(newFiles)
        checkfile = files()
        checkfilebool = newFiles in checkfile
        if checkfilebool == True:
            Rules(newFiles)
        Rules(newFiles)

class Watcher:
    DIRECTORY_TO_WATCH = config["Config"]["Source_Folder"]

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            log("Error watcher")
        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == "created":
            # Take any action here when a file is first created.
            log("Received created event - %s." % event.src_path)
            time.sleep(5)
            config, rules = loadJsons()
            time.sleep(5)
            Run_Rules()

        elif event.event_type == "modified":
            # Taken any action here when a file is modified.
            log("Received modified event - %s." % event.src_path)


if __name__ == "__main__":
    log("Starting")
    w = Watcher()
    w.run()
    log("Running")



