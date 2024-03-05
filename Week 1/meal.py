from datetime import time
def main():
    time = input('What time is it? ')
    x = convert(time)
    if x>=7 and x<=8:
        print('breakfast time')
    if x>=12 and x<=13:
        print('lunch time')
    if x>=18 and x<=19:
        print('dinner time')



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)/60
    time = hours + minutes
    return time



if __name__ == "__main__":
    main()
