def main():
    #waktu user 
    answer = input("what time is it? ")
    #memanggil fungsi convert
    time = convert(answer)
    #sarapan 7:00 dan 8:00 
    if time >= 7 and time <= 8:
        print("breakfast time")
    #makan siang 12:00 dan 13:00
    if time >= 12 and time <= 13:
        print("lunch time")
    #makan malam 18:00 dan 19:00
    if time >= 18 and time <= 19:
        print("dinner time")
def convert(time):
    #get menit dan jam
    hours, minutes = time.split(":")
    #Convert ttime ke gfloat number
    new_minute = float(minutes) / 60
    #retrun result ke main function
    return float(hours) + new_minute

if __name__ == "__main__":
    main()