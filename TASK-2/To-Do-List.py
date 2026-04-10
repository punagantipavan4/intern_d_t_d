# daily task manager
# using conpects:LIST | add/remove/view|open() file I/O
filename="tasks.txt"
# FILE HANDLING --read
# open(file,"r")-> read exisiting tasks into list 
def load_tasks():
  """read taks.txt and return a list of task strings."""
  tasks=[]
  try:
    with open(filename,"r") as f:
      for line in f:
        task=line.strip()
        if task:
          tasks.append(task)
  except FileNotFoundError:
    print("No saved taks found.starting fresh. \n")
  return tasks
  # ---------------------------------------------------
  # file Handling -write
  # open(file,"w")->save the list back to tasks.txt
  # ----------------------------------------------------
def save_tasks(tasks):
  """write tasks.txt and return a list of tasks.txt(over writes each time)"""
  with open(filename,"w") as f:
    for task in tasks:
      f.write(task+"\n")            #write each task on its own line
# --------------------------------------------------------
# Functionlity 1-add
# list method:task.append()
# -------------------------------------------------------
def add_task(tasks):
  task=input("enter task :").strip()
  if task=="":
    print("task cannot be empty.")
    return
  tasks.append(task)
  save_tasks(tasks)
  print(f'added:"{task}"')
# --------------------------------------------------------------
# functionality 2-remove
# list method:tasks.pop()
# -------------------------------------------------------------
def remove_task(tasks):
  if not tasks:
    print("no tasks to remove")
    return
  view_tasks(tasks)
  try:
    num=int(input("enter task number to remove :"))
    if 1 <= num <= len(tasks):
      removed=tasks.pop(num-1)
      save_tasks(tasks)
      print(f'removed:"{removed}"')
    else:
      print("Invalid number.")
  except ValueError:
    print("please enter a valid number.")
# -------------------------------------------------------------
# functionaly 3-view
# iterators over the list with enumerate()
# --------------------------------------------------------------
def view_tasks(tasks):
  print("\n ---your tasks---")
  if not tasks:
    print("(no tasks yet)")
  else:
    for index,task in enumerate(tasks,start=1):
      print(f"{index}.{task}")
  print(f"ToTal:{len(tasks)}task(s)")
  print("--------------------------\n")
# main menu 
def main():
  tasks=load_tasks()
 
  while True:
     print("===Task manager ===")
     print("1.view tasks")
     print("2.add task")
     print("3.Remove task")
     print("4.exit")
     choice=input("choose(1-4):").strip()
     if choice == "1":
        view_tasks(tasks)
     elif choice == "2":
        add_task(tasks)
     elif choice == "3":
        remove_task(tasks)
     elif choice == "4":
        print("tasks.saved.Good bye!")
        break
     else:
       print("Invalid Choice. Enter 1,2,3 or 4.\n")
main()
      

      




