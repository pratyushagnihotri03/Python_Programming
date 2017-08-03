while True:
    try:
        number = int(input("what is you fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure enter number")
    except ZeroDivisionError:
        print("don't pick zero")
    except:
        break
    finally:
        print("loop complete")
